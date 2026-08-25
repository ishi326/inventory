import os
from itertools import groupby
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from dotenv import load_dotenv
from database.connection import SessionLocal
from database.models import Report

load_dotenv()

router = APIRouter()

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")
serializer = URLSafeTimedSerializer(SECRET_KEY)

SESSION_MAX_AGE = 60 * 60 * 12  # 12 hours

def is_logged_in(request: Request) -> bool:
    token = request.cookies.get("admin_session")
    if not token:
        return False
    try:
        serializer.loads(token, max_age=SESSION_MAX_AGE)
        return True
    except (BadSignature, SignatureExpired):
        return False


@router.get("/login", response_class=HTMLResponse)
def login_form():
    return """
    <html>
        <body>
            <h2>Admin Login</h2>
            <form method="post" action="/login">
                <input type="password" name="password" placeholder="Password" />
                <button type="submit">Log in</button>
            </form>
        </body>
    </html>
    """


@router.post("/login")
def login_submit(password: str = Form(...)):
    if password != ADMIN_PASSWORD:
        return RedirectResponse(url="/login", status_code=303)

    token = serializer.dumps("admin")
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="admin_session", value=token, httponly=True)
    return response


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    if not is_logged_in(request):
        return RedirectResponse(url="/login")

    db = SessionLocal()
    reports = db.query(Report).order_by(Report.report_date.desc()).all()
    db.close()

    html_sections = ""
    for report_date, group in groupby(reports, key=lambda r: r.report_date):
        html_sections += f"<h3>{report_date}</h3><ul>"
        for r in group:
            if r.note:
                html_sections += f"<li>{r.store_name} — {r.sku_name}: {r.note}</li>"
            else:
                html_sections += f"<li>{r.store_name} — {r.sku_name}: send {r.qty_to_send}</li>"
        html_sections += "</ul>"

    return f"""
    <html>
        <body>
            <h1>Admin Dashboard</h1>
            <h2>Inventory Report</h2>
            {html_sections}
        </body>
    </html>
    """