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
    role = db.Column(db.String(32), index=True, unique=True, default='General')
    password_hash = db.Column(db.String(128))
    quiz = db.relationship('Quiz', backref='usersesh', lazy='dynamic')
    feedback = db.relationship('Feedbacks', backref='feedback_user', lazy='dynamic')
    long_answer = db.relationship('Long_Answers', backref='long_answer_user', lazy='dynamic')

    def __repr__(self):
        return 'Username {}'.format(self.username)

    # generate a hash for the password to be encoded
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# This is my flask_login extension class; note the helper methods
class UserLogin(UserMixin):
    def __init__(self):
        self.user_id = None

    def get_id(self):
        return self.user_id

    def get_role(self):
        return self.role

    def is_admin(self):
        return True if self.role == 'Admin' else False

    def is_general(self):
        return True if self.role == 'General' else False

    def set_role(self, role):
        self.role = role


# This is the user loader decorator
@login.user_loader
def user_loader(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        # Return blank and an anonymous user object will be instantiated
        return
    flask_user = UserLogin()
    flask_user.user_id = id
    flask_user.role = user.role
    return flask_user


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, index=True, default='0')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'short answer quiz status for {}: '.format(self.usersesh.username)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_body = db.Column(db.Text, index=True)
    long_question = db.Column(db.Boolean, default=False)
    mark_for_question = db.Column(db.Integer, index=True)
    options = db.relationship('Option', backref='question', lazy='dynamic')
    long_answer = db.relationship('Long_Answers', backref='long_question', lazy='dynamic')

    def __repr__(self):
        return 'Question {}: '.format(self.id) + '{}'.format(self.question_body)


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_body = db.Column(db.Text, index=True)
    correct = db.Column(db.Boolean, default=False, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __repr__(self):
        return 'Option: {}: '.format(self.option_body)


class Feedbacks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback_msg = db.Column(db.Text, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Long_Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, index=True)
    response = db.Column(db.Text, index=True)
    mark = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
