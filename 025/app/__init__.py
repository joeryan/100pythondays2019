from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
from app import routes, models

# from app.api import bp as api_bp
# app.register_blueprint(api_bp, url_prefix='/api')
