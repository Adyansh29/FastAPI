"""create address table

Revision ID: 2a9b3ed660e3
Revises: 39dd8a15edc4
Create Date: 2022-10-25 15:49:23.851090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a9b3ed660e3'
down_revision = '39dd8a15edc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address1", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("state", sa.String(), nullable=False),
                    sa.Column("country", sa.String(), nullable=False),
                    sa.Column("postalcode", sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("address")
