import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand

from app import db, create_app

from models.courseModel import *

#load .env into env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app, api = create_app(config_name=os.getenv('APP_SETTINGS'))


migrate = Migrate(app, db)
#manager = Manager(app)

#manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()