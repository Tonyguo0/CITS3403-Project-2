from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='GameFinder', template_mode='bootstrap3')

# __name__
from app import routes, models

from flask_admin.contrib.sqla import ModelView
from app.models import User, Post, Question, Option, Quiz

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Option, db.session))
admin.add_view(ModelView(Quiz, db.session))




