"""creates online_retail2

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
        "online_retail2",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("invoice_no", sa.String),
        sa.Column("stock_code", sa.String),
        sa.Column("description", sa.String),
        sa.Column("quantity", sa.String),
        sa.Column("invoice_date", sa.String),
        sa.Column("unit_price", sa.String),
        sa.Column("customer_id", sa.String),
        sa.Column("country", sa.String),
    )


def downgrade():
    op.drop_table("online_retail2")
