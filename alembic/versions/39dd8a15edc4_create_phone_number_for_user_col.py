"""create phone number for user col

Revision ID: 39dd8a15edc4
Revises: 
Create Date: 2022-10-25 15:40:13.606722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39dd8a15edc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "phone_number")
