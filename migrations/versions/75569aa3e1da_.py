"""empty message

Revision ID: 75569aa3e1da
Revises: c50de1acf670
Create Date: 2020-05-22 21:52:11.120940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75569aa3e1da'
down_revision = 'c50de1acf670'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_body', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_question_body'), 'question', ['question_body'], unique=False)
    op.create_table('option',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('option_body', sa.Text(), nullable=True),
    sa.Column('correct', sa.Boolean(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_option_option_body'), 'option', ['option_body'], unique=False)
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('result', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz_result'), 'quiz', ['result'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quiz_result'), table_name='quiz')
    op.drop_table('quiz')
    op.drop_index(op.f('ix_option_option_body'), table_name='option')
    op.drop_table('option')
    op.drop_index(op.f('ix_question_question_body'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###
