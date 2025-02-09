from sqlalchemy.orm import Session
from db.models import OnlineRetail2
from sqlalchemy.exc import IntegrityError


class OnlineRetail2Repository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self, limit: int = 100):
        """Retrieve all records with a limit"""
        return self.db.query(OnlineRetail2).limit(limit).all()

    def get_by_invoice(self, invoice_no: str):
        """Retrieve records by invoice number"""
        return (
            self.db.query(OnlineRetail2)
            .filter(OnlineRetail2.invoice_no == invoice_no)
            .all()
        )

    def get_by_stock_code(self, stock_code: str):
        """Retrieve records by stock code"""
        return (
            self.db.query(OnlineRetail2)
            .filter(OnlineRetail2.stock_code == stock_code)
            .all()
        )

    def get_by_customer_id(self, customer_id: int):
        """Retrieve records by customer ID"""
        return (
            self.db.query(OnlineRetail2)
            .filter(OnlineRetail2.customer_id == customer_id)
            .all()
        )

    def create(self, data: dict):
        """Insert a new record"""
        new_entry = OnlineRetail2(**data)
        try:
            self.db.add(new_entry)
            self.db.commit()
            return new_entry
        except IntegrityError as e:
            self.db.rollback()
            return None
    
    def bulk_create(self, data_list: list):
        """Insert multiple records with rollback on failure"""
        try:
            new_entries = [OnlineRetail2(**data) for data in data_list]
            self.db.add_all(new_entries)
            self.db.commit()
            return True
        except IntegrityError as e:
            self.db.rollback()
            return False

    def update(self, invoice_no: str, stock_code: str, update_data: dict):
        """Update a record"""
        record = (
            self.db.query(OnlineRetail2)
            .filter(
                OnlineRetail2.invoice_no == invoice_no,
                OnlineRetail2.stock_code == stock_code,
            )
            .first()
        )
        if record:
            for key, value in update_data.items():
                setattr(record, key, value)
            self.db.commit()
            self.db.refresh(record)
        return record

    def delete(self, invoice_no: str, stock_code: str):
        """Delete a record"""
        record = (
            self.db.query(OnlineRetail2)
            .filter(
                OnlineRetail2.invoice_no == invoice_no,
                OnlineRetail2.stock_code == stock_code,
            )
            .first()
        )
        if record:
            self.db.delete(record)
            self.db.commit()
        return record
