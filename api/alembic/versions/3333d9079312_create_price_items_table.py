"""create price_items table

Revision ID: 3333d9079312
Revises: 282ba99c1620
Create Date: 2021-01-25 18:48:03.057947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3333d9079312'
down_revision = '282ba99c1620'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'price_item',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('updated', sa.DateTime),
        sa.Column('price', sa.Float),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='cascade'))


def downgrade():
    op.drop_table('price_item')
