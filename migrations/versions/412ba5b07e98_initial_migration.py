"""Initial migration

Revision ID: 412ba5b07e98
Revises: 
Create Date: 2024-10-09 13:40:59.727537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '412ba5b07e98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ms',
    sa.Column('selected', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('retention_index', sa.String(length=256), nullable=True),
    sa.Column('num_peaks', sa.String(length=256), nullable=True),
    sa.Column('d_alkane_rt1', sa.String(length=256), nullable=True),
    sa.Column('n_alkane_rt1', sa.String(length=256), nullable=True),
    sa.Column('instrument', sa.String(length=256), nullable=True),
    sa.Column('ionization', sa.String(length=256), nullable=True),
    sa.Column('injection_method', sa.String(length=256), nullable=True),
    sa.Column('gc_column', sa.String(length=256), nullable=True),
    sa.Column('oven_temp', sa.String(length=256), nullable=True),
    sa.Column('campaign_experimental_source', sa.String(length=256), nullable=True),
    sa.Column('experimental_condition', sa.String(length=256), nullable=True),
    sa.Column('contributor', sa.String(length=256), nullable=True),
    sa.Column('date_of_entry', sa.String(length=256), nullable=True),
    sa.Column('publications', sa.String(length=256), nullable=True),
    sa.Column('x_coordinates', sa.String(length=256), nullable=True),
    sa.Column('y_coordinates', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ms')
    # ### end Alembic commands ###
