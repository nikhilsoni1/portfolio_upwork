# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, String, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OnlineRetail(Base):
    __tablename__ = 'online_retail'
    __table_args__ = (
        UniqueConstraint('InvoiceNo', 'StockCode'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('online_retail_id_seq'::regclass)"))
    InvoiceNo = Column(String(20), nullable=False)
    StockCode = Column(String(20), nullable=False)
    Description = Column(String(255))
    Quantity = Column(Integer, nullable=False)
    InvoiceDate = Column(DateTime, nullable=False)
    UnitPrice = Column(Float(53), nullable=False)
    CustomerID = Column(Integer)
    Country = Column(String(100), nullable=False)
