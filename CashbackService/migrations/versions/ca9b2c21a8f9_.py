"""empty message

Revision ID: ca9b2c21a8f9
Revises: 
Create Date: 2019-07-28 22:56:28.125669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca9b2c21a8f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notify',
    sa.Column('user_id', sa.String(length=10), nullable=False),
    sa.Column('parking_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notify')
    # ### end Alembic commands ###
