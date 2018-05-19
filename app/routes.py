
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, CreateReportForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Persona, Usuario, CatalogoDelito, CatalogoHorario, \
    CatalogoFuenteInfo, Reporte, CatalogoSexo
from datetime import date


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
        db.session.add(person)
        db.session.commit()
        user = Usuario(correo=form.email.data, persona_id=person.id, sexo_id=form.sex.data, fecha_nac=form.birthdate.data)
        db.session.add(user)
        db.session.commit()
        flash('El usuario ha sido registrado exitosamente!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/create_report', methods=['GET', 'POST'])
@login_required
def create_report():
    form = CreateReportForm()
    form.crime.choices = [(c.id, c.descripcion) for c in CatalogoDelito.query.all()]
    form.hour.choices = [(h.id, h.descripcion) for h in CatalogoHorario.query.all()]
    form.reference.choices = [(r.id, r.descripcion) for r in CatalogoFuenteInfo.query.all()]
    if form.validate_on_submit():
        lat = float(form.coordinates_lat.data)
        lng = float(form.coordinates_lng.data)
        zone = int(form.zone.data)
        user = Usuario.query.filter_by(persona_id=current_user.id).first_or_404()
        report = Reporte(usuario_id=user.id, fecha=form.date.data, delito_id=form.crime.data,
            hora_delito_id=form.hour.data, detalles=form.details.data, latitud=lat, longitud=lng, sector=zone)
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('index'))    
    return render_template('create_report.html', title='Crear Reporte', active='add_report',
        form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    persona = Persona.query.filter_by(username=username).first_or_404()
    usuario = Usuario.query.filter_by(persona_id=current_user.id).first_or_404() 
    sexo = CatalogoSexo.query.filter_by(id=usuario.sexo_id).first()
    return render_template('profile.html', title='Perfil de usuario', active='user_profile',
        persona=persona, usuario=usuario, sexo=sexo.descripcion)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.nombre = form.name.data
        user = Usuario.query.filter_by(persona_id = current_user.id).first_or_404()
        user.sexo_id = form.sex.data
        db.session.commit()
        flash('Tus cambios han sido guardados.')
        return redirect(url_for( 'user', username=current_user.username ) )
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.name.data = current_user.nombre
    return render_template('edit_profile.html', title='Editar Perfil',
                           form=form)
