"""
This module contains the logic for determining when to reorder inventory items based on their current stock levels and predefined thresholds. 
The reorder process is triggered when the stock level of an item falls below the specified REVIEW_THRESHOLD, which is set to 100 units.
"""
REVIEW_THRESHOLD = 100

def compare_to_reorder_levels(extracted_items, reorder_map):
    report_rows = []
    for item in extracted_items:
        sku = item["sku"]
        quantity = item["quantity"]
        if quantity <= -1:
            report_rows.append({
                "sku_name": sku,
                "qty_to_send": None,
                "note": "Illegible on sheet — please verify manually"
            })
            continue
        if quantity > REVIEW_THRESHOLD:
            report_rows.append({
                "sku_name": sku,
                "qty_to_send": None,
                "note": f"Unusually high quantity ({quantity}) — please verify"
            })
            continue
        ref = reorder_map.get(sku)
        if not ref:
            continue  # SKU wasn't in your reorder levels list at all — skipped for now
        if quantity < ref["reorder_level"]:
            report_rows.append({
                "sku_name": sku,
                "qty_to_send": ref["moq"],
                "note": None
            })

    return report_rows