# Models.py is model used to build the database using flask sqlAlchemy and flask migrate


from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# structure for the User to login etc...
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default = False)
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

# structure for the Quiz which stores the result of the short answer question section for a user
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, index=True, default = '0')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'short answer quiz status for {}: '.format(self.usersesh.username)

# structure for the questions, stores if is a long or short answer question, mark for each question and the text of the question
class Question (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_body = db.Column(db.Text, index=True)
    long_question = db.Column(db.Boolean, default = False)
    mark_for_question = db.Column(db.Integer, index = True, default = "1")
    options = db.relationship('Option', backref='question', lazy='dynamic')
    long_answer = db.relationship('Long_Answers', backref='long_question', lazy='dynamic')

    def __repr__(self):
        return 'Question {}: '.format(self.id) + '{}'.format(self.question_body)

# structure for the Option which stores the options for short answer questions and indicates which option is correct
class Option (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_body = db.Column(db.Text, index=True)
    correct = db.Column(db.Boolean, default = False, nullable=False)
    question_id =db.Column(db.Integer, db.ForeignKey('question.id'))

    def __repr__(self):
        return 'Option: {}: '.format(self.option_body)

# structure for the feedback of the users with the user's feedback message stored 
class Feedbacks (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback_msg = db.Column(db.Text, index=True)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'))

# structure of the Long_answers correlating to which user has answered which question, also stores the mark which will be manually given and the response from the admin
class Long_Answers (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, index=True)
    response = db.Column(db.Text, index=True)
    mark = db.Column(db.Integer, index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
