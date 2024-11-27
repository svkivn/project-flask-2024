"""Add user_id to Post

Revision ID: b4fe7fa08c01
Revises: c77671a08cf5
Create Date: 2024-11-27 17:52:41.255917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4fe7fa08c01'
down_revision = 'c77671a08cf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('user_id', 'users', ['user_id'], ['id'])
        batch_op.drop_column('author')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
