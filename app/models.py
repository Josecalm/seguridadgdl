from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class CrimeList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))

    report = db.relationship('Report', backref='crime', lazy=True)


class ChatStatusList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15))

    chat_status = db.relationship('Chat', backref='status_chat', lazy=True)


class ReportStatusList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15))

    report_status = db.relationship('Report', backref='status_report', lazy=True)


class ReferenceInfoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))

    report_reference = db.relationship('Report', backref='reference_report', lazy=True)


class HourList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15))

    hour_crime_report = db.relationship('Report', backref='hour', lazy=True)


class SexList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15))

    person_sex = db.relationship('Person', backref='sex_person', lazy=True)
    victim_sex = db.relationship('Victim', backref='sex_victim', lazy=True)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_time = db.Column(db.DateTime, default=datetime.utcnow)
    response_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('chat_status_list.id'))

    user = db.relationship('User', foreign_keys='Chat.user_id')
    agent = db.relationship('User', foreign_keys='Chat.user_id')


class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    sex_id = db.Column(db.Integer, db.ForeignKey('sex_list.id'))

    report_victim = db.relationship('Report', backref='victim_report', lazy=True)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(100), unique=True)
    is_admin = db.Column(db.Boolean, default=False)

    person_user = db.relationship('Person', backref='user_person', lazy=True)
    report_user = db.relationship('Report', backref='Report.user_id',
        primaryjoin='User.id==Report.user_id', lazy='dynamic')
    chat_user = db.relationship('Chat', backref='Chat.user_id',
        primaryjoin='User.id==Chat.user_id', lazy='dynamic')

    def __repr__(self):
        return '<User #{}: {} Admin: {}>'.format(self.id, self.username, self.is_admin)

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    birthdate = db.Column(db.DateTime)
    sex_id = db.Column(db.Integer, db.ForeignKey('sex_list.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    crime_id = db.Column(db.Integer, db.ForeignKey('crime_list.id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    crime_hour_id = db.Column(db.Integer, db.ForeignKey('hour_list.id'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    zone = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey('report_status_list.id'))
    details = db.Column(db.Text)
    victim_id = db.Column(db.Integer, db.ForeignKey('victim.id'))
    reference_id = db.Column(db.Integer, db.ForeignKey('reference_info_list.id'))

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35))
    coordinates = db.Column(db.JSON)

class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    polygon = db.Column(db.JSON)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
