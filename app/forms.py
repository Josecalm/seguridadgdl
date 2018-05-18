from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField, HiddenField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Persona, Usuario, CatalogoDelito
from datetime import date

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    password2 = PasswordField('Repita contrasena', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = Persona.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor ingresa otro nombre de usuario.')

    def validate_email(self, email):
        user = Usuario.query.filter_by(correo=email.data).first()
        if user is not None:
            raise ValidationError('Ya existe un usuario registrado con ese correo. Por favor ingrese otro.')

class CreateReportForm(FlaskForm):
    crime = SelectField('Tipo de delito', coerce=int)
    hour = SelectField('Horario', coerce=int)
    reference = SelectField('Fuente información', coerce=int)
    date = DateField('Fecha', format='%d-%m-%Y')
    details = TextAreaField()
    submit = SubmitField('Crear reporte')
    coordinates_lng = HiddenField()
    coordinates_lat = HiddenField()
    zone = HiddenField()
