from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    quiz = db.relationship('Quiz', backref='usersesh', lazy='dynamic')
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}> and '.format(self.username) + '<Email {}>'.format(self.email)
    # generate a hash for the password to be encoded 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, index=True, default = '0')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Question (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_body = db.Column(db.Text, index=True)
    options = db.relationship('Option', backref='question', lazy='dynamic')

class Option (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_body = db.Column(db.Text, index=True)
    correct = db.Column(db.Boolean, default = False, nullable=False)
    question_id =db.Column(db.Integer, db.ForeignKey('question.id'))



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
