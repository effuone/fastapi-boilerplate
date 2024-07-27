"""products_added

Revision ID: c4e8bcd6bc0b
Revises:
Create Date: 2024-07-26 14:36:35.812670

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "c4e8bcd6bc0b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("products_pkey")),
    )
    op.create_index(op.f("products_id_idx"), "products", ["id"], unique=False)
    op.create_index(op.f("products_name_idx"), "products", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("products_name_idx"), table_name="products")
    op.drop_index(op.f("products_id_idx"), table_name="products")
    op.drop_table("products")
    # ### end Alembic commands ###
