"""add product table

Revision ID: 282ba99c1620
Revises: 0da071ff6b96
Create Date: 2021-01-25 18:18:51.750430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282ba99c1620'
down_revision = '0da071ff6b96'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('name', sa.String(100), unique=True),
        sa.Column('description', sa.String(400)),
        sa.Column('image', sa.String(300))        
    )



def downgrade():
    op.drop_table('products')
