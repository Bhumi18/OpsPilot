"""create payments table

Revision ID: 001_create_payments_table
Revises: 
Create Date: 2026-09-15 18:46:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '001_create_payments_table'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'payments',
        sa.Column('payment_id', sa.String(length=50), nullable=False),
        sa.Column('customer_id', sa.String(length=100), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('processing_time_ms', sa.Float(), nullable=False, server_default='0.0'),
        sa.PrimaryKeyConstraint('payment_id')
    )
    op.create_index(op.f('ix_payments_payment_id'), 'payments', ['payment_id'], unique=False)
    op.create_index(op.f('ix_payments_customer_id'), 'payments', ['customer_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_payments_customer_id'), table_name='payments')
    op.drop_index(op.f('ix_payments_payment_id'), table_name='payments')
    op.drop_table('payments')
