"""report table coord attr

Revision ID: bb7499198bfa
Revises: c2a673754978
Create Date: 2018-05-17 21:39:38.123327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb7499198bfa'
down_revision = 'c2a673754978'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reporte', sa.Column('latitud', sa.Float(), nullable=True))
    op.add_column('reporte', sa.Column('longitud', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reporte', 'longitud')
    op.drop_column('reporte', 'latitud')
    # ### end Alembic commands ###
