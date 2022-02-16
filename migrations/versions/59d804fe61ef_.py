"""empty message

Revision ID: 59d804fe61ef
Revises: 275f51c12714
Create Date: 2022-02-16 17:32:37.482834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '59d804fe61ef'
down_revision = '275f51c12714'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('baseinfo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=3), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('date', sa.String(length=30), nullable=True),
    sa.Column('responseheader', sa.Text(), nullable=True),
    sa.Column('Server', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scanTask',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tid', sa.String(length=128), nullable=False),
    sa.Column('starttime', sa.String(length=30), nullable=False),
    sa.Column('endtime', sa.String(length=30), nullable=False),
    sa.Column('key', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('scantask')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scantask',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('tid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('starttime', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('endtime', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('key', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('scanTask')
    op.drop_table('baseinfo')
    # ### end Alembic commands ###
