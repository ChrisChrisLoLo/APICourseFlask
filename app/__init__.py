import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local import
from app.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app():
    """
    Initialize the Flask app, the SQLAlchemy db, and the Flask-Restful Api
    Configurates the app based on the app.config, which is selected from a .env file.
    Sets up migration commands for the flask cli
    """
    app = Flask(__name__)

    app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy()
    db.init_app(app)

    api = Api(app)

    # Create migration commands
    migrate = Migrate(app,db)

    return app, api