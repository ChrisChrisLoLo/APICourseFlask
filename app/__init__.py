import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from app.config import app_config

# Create app instance and configure it.
app = Flask(__name__)

app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
# Import scripts after db is defined to prevent circular dependencies.
from app.scripts import seedFromCSV 


api = Api(app)

# Create function to seed database
# Call using `flask seed_db`
@app.cli.command()
def seed_db():
    seedFromCSV()


# Create migration commands
# Call using `flask db _____`
migrate = Migrate(app,db)
