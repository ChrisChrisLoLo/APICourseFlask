import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initialize sql-alchemy
db = SQLAlchemy()

# local import
# Placed after db declaration to prevent circular dependencies.
# TODO: This is likely a poor practice, and create_app should
# be moved to a new file entirely 
from app.config import app_config
from app.scripts import seedFromCSV 


def create_app():
    """
    Initialize the Flask app, the SQLAlchemy db, and the Flask-Restful Api
    Configurates the app based on the app.config, which is selected from a .env file.
    Sets up migration commands for the flask cli
    """
    app = Flask(__name__)

    app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app)

    # Create function to seed database
    # Call using `flask seed_db`
    @app.cli.command()
    def seed_db():
        seedFromCSV(db)


    # Create migration commands
    # Call using `flask db _____`
    migrate = Migrate(app,db)

    return app, api