"""empty message

Revision ID: a829be26b238
Revises: d6f26de54e04
Create Date: 2021-03-27 21:37:16.239207

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a829be26b238'
down_revision = 'd6f26de54e04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_subtask_mapping',
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('subtask_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['subtask_id'], ['subtask.id'], )
    )
    op.drop_constraint('item_ibfk_1', 'item', type_='foreignkey')
    op.drop_column('item', 'subtask_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('subtask_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('item_ibfk_1', 'item', 'subtask', ['subtask_id'], ['id'])
    op.drop_table('item_subtask_mapping')
    # ### end Alembic commands ###