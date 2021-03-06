"""initial version

Revision ID: 00353cb9b31d
Revises: 
Create Date: 2018-05-12 21:54:29.428703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00353cb9b31d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalogo_delito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catalogo_estado_chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catalogo_estado_reporte',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catalogo_fuente_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fuente_descripcion', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catalogo_horario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catalogo_sexo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mapa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poligono', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('contrasena', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_persona_username'), 'persona', ['username'], unique=True)
    op.create_table('sector',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=35), nullable=True),
    sa.Column('coordenadas', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('difunto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.Column('sexo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sexo_id'], ['catalogo_sexo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('persona_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['persona_id'], ['persona.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_nac', sa.DateTime(), nullable=True),
    sa.Column('sexo_id', sa.Integer(), nullable=True),
    sa.Column('correo', sa.String(length=100), nullable=True),
    sa.Column('persona_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['persona_id'], ['persona.id'], ),
    sa.ForeignKeyConstraint(['sexo_id'], ['catalogo_sexo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hora_peticion', sa.DateTime(), nullable=True),
    sa.Column('hora_respuesta', sa.DateTime(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('operador_id', sa.Integer(), nullable=True),
    sa.Column('estado_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['estado_id'], ['catalogo_estado_chat.id'], ),
    sa.ForeignKeyConstraint(['operador_id'], ['operador.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reporte',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.Column('delito_id', sa.Integer(), nullable=True),
    sa.Column('operador_id', sa.Integer(), nullable=True),
    sa.Column('hora_delito_id', sa.Integer(), nullable=True),
    sa.Column('sector', sa.Integer(), nullable=True),
    sa.Column('estado_id', sa.Integer(), nullable=True),
    sa.Column('detalles', sa.Text(), nullable=True),
    sa.Column('difunto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['delito_id'], ['catalogo_delito.id'], ),
    sa.ForeignKeyConstraint(['difunto_id'], ['difunto.id'], ),
    sa.ForeignKeyConstraint(['estado_id'], ['catalogo_estado_reporte.id'], ),
    sa.ForeignKeyConstraint(['hora_delito_id'], ['catalogo_horario.id'], ),
    sa.ForeignKeyConstraint(['operador_id'], ['operador.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reporte')
    op.drop_table('chat')
    op.drop_table('usuario')
    op.drop_table('operador')
    op.drop_table('difunto')
    op.drop_table('sector')
    op.drop_index(op.f('ix_persona_username'), table_name='persona')
    op.drop_table('persona')
    op.drop_table('mapa')
    op.drop_table('catalogo_sexo')
    op.drop_table('catalogo_horario')
    op.drop_table('catalogo_fuente_info')
    op.drop_table('catalogo_estado_reporte')
    op.drop_table('catalogo_estado_chat')
    op.drop_table('catalogo_delito')
    # ### end Alembic commands ###
