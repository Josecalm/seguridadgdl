
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, CreateReportForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Person, User, CrimeList, HourList, \
    ReferenceInfoList, Report, SexList
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
        user = User.query.filter_by(username=form.username.data).first()
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
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        person = Person(name=form.name.data, user_id=user.id, sex_id=form.sex.data, birthdate=form.birthdate.data)
        db.session.add(person)
        db.session.commit()
        flash('El usuario ha sido registrado exitosamente!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/create_report', methods=['GET', 'POST'])
@login_required
def create_report():
    form = CreateReportForm()
    if form.validate_on_submit():
        lat = float(form.coordinates_lat.data)
        lng = float(form.coordinates_lng.data)
        zone = int(form.zone.data)
        report = Report(user_id=current_user.id, date=form.date.data, crime_id=form.crime.data,
            crime_hour_id=form.hour.data, latitude=lat, longitude=lng, zone=zone, details=form.details.data, reference_id=form.reference.data)
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('index'))    
    return render_template('create_report.html', title='Crear Report', active='add_report',
        form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(id=current_user.id).first_or_404()
    person = Person.query.filter_by(user_id=current_user.id).first_or_404() 
    sex = SexList.query.filter_by(id=person.sex_id).first()
    return render_template('profile.html', title='Perfil de usuario', active='user_profile',
        person=person, user=user, sex=sex.description)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    person = Person.query.filter_by(user_id = current_user.id).first_or_404()
    if form.validate_on_submit():        
        current_user.username = form.username.data
        person.name = form.name.data
        person.sex_id = form.sex.data
        db.session.commit()
        flash('Tus cambios han sido guardados.')
        return redirect(url_for( 'user', username=current_user.username ) )
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.name.data = person.name
    return render_template('edit_profile.html', title='Editar Perfil',
                           form=form)
