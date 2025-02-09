"""creates online_retail

Revision ID: ddf9610d4ef0
Revises:
Create Date: 2025-02-08 22:47:22.534673

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ddf9610d4ef0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "online_retail",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("InvoiceNo", sa.String(20), nullable=False),
        sa.Column("StockCode", sa.String(20), nullable=False),
        sa.Column("Description", sa.String(255), nullable=True),
        sa.Column("Quantity", sa.Integer, nullable=False),
        sa.Column("InvoiceDate", sa.DateTime, nullable=False),
        sa.Column("UnitPrice", sa.Float, nullable=False),
        sa.Column("CustomerID", sa.Integer, nullable=True),
        sa.Column("Country", sa.String(100), nullable=False),
        sa.UniqueConstraint("InvoiceNo", "StockCode", name="uq_invoice_stock"),
    )


def downgrade():
    op.drop_table("online_retail")
