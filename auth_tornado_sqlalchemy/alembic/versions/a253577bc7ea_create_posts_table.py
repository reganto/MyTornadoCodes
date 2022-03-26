"""create posts table

Revision ID: a253577bc7ea
Revises: 
Create Date: 2020-01-22 15:11:55.652649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a253577bc7ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('headline', sa.String(200), nullable=False),
        sa.Column('content', sa.String(200)),
    )


def downgrade():
    op.drop_table('posts', 'testdb')
