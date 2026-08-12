from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Boolean
from database.connection import Base

class Store(Base):
    __tablename__ = "stores"
    store_code = Column(String(4), primary_key=True)
    name = Column(String)
    city = Column(String)
    type = Column(String)
    active = Column(Boolean, default=True)

class ReorderLevel(Base):
    __tablename__ = "reorder_levels"
    sku_name = Column(String, primary_key=True)
    reorder_level = Column(Integer)
    moq = Column(Integer)

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_code = Column(String(4), ForeignKey("stores.store_code"))
    submitted_at = Column(DateTime)
    photo_url = Column(String)
    status = Column(String)

class ExtractedItem(Base):
    __tablename__ = "extracted_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"))
    sku_name = Column(String)
    quantity = Column(Integer)

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(Date)
    store_code = Column(String(4), ForeignKey("stores.store_code"))
    store_name = Column(String)
    sku_name = Column(String)
    qty_to_send = Column(Integer)
    note = Column(String, nullable=True)

class AdminUser(Base):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String)