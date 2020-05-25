from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

# initialise the application as well as our database, login manager and admin
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='GameFinder', template_mode='bootstrap3')

# import the following after we have initialised our app so we have a cycle
from app import routes, models
from flask_admin.contrib.sqla import ModelView
from app.models import User, Question, Option, Quiz, Feedbacks, Long_Answers

# add all of our desired views to the admin panel
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Option, db.session))
admin.add_view(ModelView(Quiz, db.session))
admin.add_view(ModelView(Feedbacks, db.session))
admin.add_view(ModelView(Long_Answers, db.session))




