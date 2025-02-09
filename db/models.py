# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OnlineRetail2(Base):
    __tablename__ = 'online_retail2'

    id = Column(Integer, primary_key=True, server_default=text("nextval('online_retail2_id_seq'::regclass)"))
    invoice_no = Column(String)
    stock_code = Column(String)
    description = Column(String)
    quantity = Column(String)
    invoice_date = Column(String)
    unit_price = Column(String)
    customer_id = Column(String)
    country = Column(String)
