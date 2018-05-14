from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, CreateReportForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Persona, Usuario, CatalogoDelito, CatalogoHorario, \
    CatalogoFuenteInfo

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Inicio', active='maps')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Persona.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nombre de usuario o contrasena no validos!')        
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Ingresar', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        person = Persona(username=form.username.data, nombre=form.name.data)
        person.set_password(form.password.data)
        user = Usuario(correo=form.email.data, persona_id=person.id)
        db.session.add(person)
        db.session.add(user)
        db.session.commit()
        flash('El usuario ha sido registrado exitosamente!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/createreport')
@login_required
def create_report():
    form = CreateReportForm()
    form.crime.choices = [(c.id, c.descripcion) for c in CatalogoDelito.query.all()]
    form.hour.choices = [(h.id, h.descripcion) for h in CatalogoHorario.query.all()]
    form.reference.choices = [(r.id, r.descripcion) for r in CatalogoFuenteInfo.query.all()]    
    return render_template('create_report.html', title='Crear Reporte', active='add_report',
        form=form)
