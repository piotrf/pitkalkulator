"""empty message

Revision ID: 5bf04708c9f5
Revises: d33c2b07bf9e
Create Date: 2020-11-16 23:02:24.584101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bf04708c9f5'
down_revision = 'd33c2b07bf9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('created_at', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity', 'created_at')
    # ### end Alembic commands ###
