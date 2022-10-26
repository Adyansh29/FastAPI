"""add a apartment number

Revision ID: 05a4cd1a0c0d
Revises: f3fa400ff4c0
Create Date: 2022-10-25 17:10:18.041135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05a4cd1a0c0d'
down_revision = 'f3fa400ff4c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")