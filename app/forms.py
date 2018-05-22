from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField, HiddenField, validators
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import date
from app.models import Person, User, CrimeList, SexList, ReferenceInfoList, HourList, ReportStatusList

class LoginForm(FlaskForm):
    username = StringField('Userio', validators=[DataRequired()])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    password2 = PasswordField('Repita contrasena', validators=[DataRequired(), EqualTo('password')])
    sex = SelectField('Sexo', coerce=int, choices = [(s.id, s.description) for s in SexList.query.all()], default = 2)
    birthdate = DateField('Fecha de Nacimiento', [validators.Required()], format='%d-%m-%Y')
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor ingresa otro nombre de usuario.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Ya existe un usuario registrado con ese correo. Por favor ingrese otro.')

class CreateReportForm(FlaskForm):
    crime = SelectField('Tipo de delito', coerce=int, choices = [(c.id, c.description) for c in CrimeList.query.all()])
    hour = SelectField('Horario', coerce=int, choices = [(h.id, h.description) for h in HourList.query.all()])
    reference = SelectField('Fuente información', coerce=int, choices = [(r.id, r.description) for r in ReferenceInfoList.query.all()])
    date = DateField('Fecha', format='%d-%m-%Y')
    details = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Crear reporte')
    coordinates_lng = HiddenField()
    coordinates_lat = HiddenField()
    zone = HiddenField()

class EditProfileForm(FlaskForm):
    name = TextAreaField('Nombre', validators=[DataRequired()])
    username = TextAreaField('Username', validators=[DataRequired()])
    sex = SelectField('Sexo', coerce=int, choices = [(s.id, s.description) for s in SexList.query.all()] )
    submit = SubmitField('Guardar información')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if ((user is not None) and (user.username != username.data)):
            raise ValidationError('Por favor ingresa otro nombre de usuario.')

class EditStatusReport(FlaskForm):
    report_id = HiddenField()
    status = SelectField('Estado', coerce=int, choices = [(s.id, s.description) for s in ReportStatusList.query.all()], default = 1 )
    status_details = TextAreaField('Detalles del estado', validators=[DataRequired()])
    coordinates_lng = HiddenField()
    coordinates_lat = HiddenField()
    submit = SubmitField('Guardar cambios')


