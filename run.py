import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import app_config
from controllers import courseController


### INITIALIZATION
# Initialize the Flask app, the SQLAlchemy db, and the Flask-Restful Api
# Configurates the app based on the app.config, which is selected from a .env file.
# Sets up migration commands for the flask cli
app = Flask(__name__)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

api = Api(app)

migrate = Migrate(app,db)

### ROUTING
# The routing will occur in run.py for now. A new routing file may need to
# be created for cleaner code seperation. 
courseController.routeCourses(api)


### MAIN
if __name__ == '__main__':
    app.run()