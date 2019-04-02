from flask import Flask
from config import Config

application = Flask(__name__)
application.config.from_object(Config)
from app import routes

# from app.api import bp as api_bp
# app.register_blueprint(api_bp, url_prefix='/api')
