"""empty message

Revision ID: 658425a142f8
Revises: 
Create Date: 2022-09-02 18:36:53.547844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '658425a142f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column(
        'rating', sa.Integer(), nullable=True))
    op.execute('UPDATE questions SET rating = 1 WHERE rating IS NULL')
    # op.drop_constraint('category', 'questions', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_foreign_key('category', 'questions', 'categories', ['category'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.drop_column('questions', 'rating')
    # ### end Alembic commands ###
