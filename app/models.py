from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class CatalogoDelito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))

    reporte = db.relationship('Reporte', backref='delito', lazy=True)


class CatalogoEstadoChat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(15))

    chat_estado = db.relationship('Chat', backref='estado_chat', lazy=True)


class CatalogoEstadoReporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(15))

    reporte_estado = db.relationship('Reporte', backref='estado_reporte', lazy=True)


class CatalogoFuenteInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20))


class CatalogoHorario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(15))

    horario_delito_reporte = db.relationship('Reporte', backref='horario', lazy=True)


class CatalogoSexo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(15))

    usuario_sexo = db.relationship('Usuario', backref='sexo_usuario', lazy=True)
    difunto_sexo = db.relationship('Difunto', backref='sexo_difunto', lazy=True)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hora_peticion = db.Column(db.DateTime, default=datetime.utcnow)
    hora_respuesta = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    operador_id = db.Column(db.Integer, db.ForeignKey('operador.id'))
    estado_id = db.Column(db.Integer, db.ForeignKey('catalogo_estado_chat.id'))

class Difunto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    sexo_id = db.Column(db.Integer, db.ForeignKey('catalogo_sexo.id'))

    reporte_difunto = db.relationship('Reporte', backref='difunto_reporte', lazy=True)


class Operador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))

    reporte_operador = db.relationship('Reporte', backref='operador_reporte', lazy=True)
    chat_operador = db.relationship('Chat', backref='operador_chat', lazy=True)


class Persona(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    username = db.Column(db.String(20), index=True, unique=True)
    contrasena = db.Column(db.String(128))

    usuario_persona = db.relationship('Usuario', backref='persona_usuario', lazy=True)
    usuario_operador = db.relationship('Operador', backref='persona_operador', lazy=True)

    def __repr__(self):
        return '<Persona #{}: {}>'.format(self.id, self.username)

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")

    def set_password(self, password):
        self.contrasena = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)


class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    delito_id = db.Column(db.Integer, db.ForeignKey('catalogo_delito.id'))
    operador_id = db.Column(db.Integer, db.ForeignKey('operador.id'))
    hora_delito_id = db.Column(db.Integer, db.ForeignKey('catalogo_horario.id'))
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    sector = db.Column(db.Integer)
    estado_id = db.Column(db.Integer, db.ForeignKey('catalogo_estado_reporte.id'))
    detalles = db.Column(db.Text)
    difunto_id = db.Column(db.Integer, db.ForeignKey('difunto.id'))


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_nac = db.Column(db.DateTime)
    sexo_id = db.Column(db.Integer, db.ForeignKey('catalogo_sexo.id'))
    correo = db.Column(db.String(100), unique=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))

    reporte_usuario = db.relationship('Reporte', backref='usuario_reporte', lazy=True)
    chat_usuario = db.relationship('Chat', backref='usuario_reporte', lazy=True)

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(35))
    coordenadas = db.Column(db.JSON)

class Mapa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poligono = db.Column(db.JSON)

@login.user_loader
def load_user(id):
    return Persona.query.get(int(id))
