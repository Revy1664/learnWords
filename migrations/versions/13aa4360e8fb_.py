"""empty message

Revision ID: 13aa4360e8fb
Revises: ffb6c0421531
Create Date: 2024-09-23 20:58:59.597564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13aa4360e8fb'
down_revision = 'ffb6c0421531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
