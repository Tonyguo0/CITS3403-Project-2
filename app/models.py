from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#  Flask-Login retrieves the ID of the user from the session, and then loads that user into memory
# Flask-Login knows nothing about databases, it needs the application's help in loading a user.

# The id that Flask-Login passes to the function as an argument is going 
# to be a string, so databases that use numeric IDs need to convert the 
# string to integer as you see above.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    roles = db.relationship('Role', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}> and '.format(self.username) + '<Email {}>'.format(self.email) 
    # generate a hash for the password to be encoded 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)