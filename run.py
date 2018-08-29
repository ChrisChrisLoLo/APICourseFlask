import os

from app import create_app
from controllers import courseController

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app, api = create_app(config_name)

#The routing will occur in run.py for now. A new routing file may need to
#be created for cleaner code seperation. 
courseController.routeCourses(api)

if __name__ == '__main__':
    app.run()