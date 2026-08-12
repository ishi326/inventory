from database.connection import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("ALTER TABLE reports ADD COLUMN IF NOT EXISTS note VARCHAR;"))
    conn.commit()
print("Column added.")