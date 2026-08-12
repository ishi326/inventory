from fastapi import APIRouter, Form, UploadFile, File
from datetime import datetime, date
from services.gemini import extract_inventory_from_photo
from services.reorder import compare_to_reorder_levels
from database.connection import SessionLocal
from database.models import ReorderLevel, Submission, ExtractedItem, Report, Store

router = APIRouter()

@router.post("/submit")
async def submit_inventory(store_code: str = Form(...), photo: UploadFile = File(...)):
    photo_bytes = await photo.read()

    db = SessionLocal()

    reorder_map = {
        row.sku_name: {"reorder_level": row.reorder_level, "moq": row.moq}
        for row in db.query(ReorderLevel).all()
    }
    known_skus = list(reorder_map.keys())

    extracted_items = extract_inventory_from_photo(photo_bytes, photo.content_type, known_skus)

    new_submission = Submission(
        store_code=store_code,
        submitted_at=datetime.now(),
        photo_url=None,
        status="processed"
    )
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    submission_id = new_submission.id

    for item in extracted_items:
        db.add(ExtractedItem(
            submission_id=submission_id,
            sku_name=item["sku"],
            quantity=item["quantity"]
        ))
    db.commit()

    store = db.query(Store).filter(Store.store_code == store_code).first()
    store_name = store.name if store else "Unknown store"

    report_rows = compare_to_reorder_levels(extracted_items, reorder_map)

    for row in report_rows:
        db.add(Report(
            report_date=date.today(),
            store_code=store_code,
            store_name=store_name,
            sku_name=row["sku_name"],
            qty_to_send=row["qty_to_send"],
            note=row["note"]
        ))
    db.commit()
    db.close()

    return {
        "store_code": store_code,
        "submission_id": submission_id,
        "extracted_items": extracted_items,
        "report_rows": report_rows
    }
