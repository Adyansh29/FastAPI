"""create address_id to users

Revision ID: f3fa400ff4c0
Revises: 2a9b3ed660e3
Create Date: 2022-10-25 16:00:25.340889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3fa400ff4c0'
down_revision = '2a9b3ed660e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key("address_users_fk", source_table="users", referent_table="address",
                          local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")

