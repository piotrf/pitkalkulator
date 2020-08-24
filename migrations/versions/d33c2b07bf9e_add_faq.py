"""empty message

Revision ID: d33c2b07bf9e
Revises: 5d56fca61f26
Create Date: 2020-09-06 05:57:44.276625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd33c2b07bf9e'
down_revision = '5d56fca61f26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faq',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=128), nullable=True),
    sa.Column('answer', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('faq')
    # ### end Alembic commands ###
