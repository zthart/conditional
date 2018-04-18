"""Add Semester Enum to Co-Op Table

Revision ID: 2c3193839c9d
Revises: 6ae578b76143
Create Date: 2017-05-24 00:18:22.645256

"""

# revision identifiers, used by Alembic.
revision = '2c3193839c9d'
down_revision = '6ae578b76143'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    semester = postgresql.ENUM('Fall', 'Spring', 'Neither', name='co_op_enum')
    semester.create(op.get_bind())
    op.add_column('current_coops', sa.Column('semester', sa.Enum('Fall', 'Spring', 'Neither', name='co_op_enum'), server_default='Neither', nullable=False))
    op.drop_column('current_coops', 'active')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('current_coops', sa.Column('active', sa.BOOLEAN(), server_default=sa.sql.expression.true(), autoincrement=False, nullable=False))
    op.drop_column('current_coops', 'semester')
    ### end Alembic commands ###