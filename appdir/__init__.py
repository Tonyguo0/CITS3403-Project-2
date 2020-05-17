from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

appvar = Flask(__name__)
appvar.config.from_object(Config)
db = SQLAlchemy(appvar)
migrate = Migrate(appvar, db)
# __name__
from appdir import routes, models
