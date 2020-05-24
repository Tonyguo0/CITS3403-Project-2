"""empty message

Revision ID: 3c676ea1a187
Revises: b3aa9dd39f9f
Create Date: 2020-05-24 22:39:19.505471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c676ea1a187'
down_revision = 'b3aa9dd39f9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('mark_for_question', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_question_mark_for_question'), 'question', ['mark_for_question'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_mark_for_question'), table_name='question')
    op.drop_column('question', 'mark_for_question')
    # ### end Alembic commands ###
