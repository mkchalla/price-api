"""create user table

Revision ID: 0da071ff6b96
Revises: 
Create Date: 2021-01-02 15:54:40.928550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0da071ff6b96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(100), unique=True),
        sa.Column('hashed_password', sa.String(100)),
        sa.Column('email', sa.String(200)),
        sa.Column('created_date', sa.DateTime),
        sa.Column('is_active', sa.Boolean)
    )


def downgrade():
    op.drop_table('users')
