"""empty message

Revision ID: b3aa9dd39f9f
Revises: 75569aa3e1da
Create Date: 2020-05-24 20:01:32.020882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3aa9dd39f9f'
down_revision = '75569aa3e1da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('long_question', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'long_question')
    # ### end Alembic commands ###
