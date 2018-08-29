import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# local import
from app.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    print(app_config[config_name])
    #app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    #TODO: App.config.from_x doesn't seem to work currently so configs are hard coded in.
    #This should be figured out and fix when possible
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['DEBUG'] = True 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print(app.config)
    db.init_app(app)

    return app, api