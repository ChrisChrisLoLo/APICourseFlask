import os

from app import app, api
from app.config import app_config
from controllers import courseController


### INITIALIZATION
# Initialize the flask app,api,db, and any commands

### ROUTING
# The routing will occur in run.py for now. A new routing file may need to
# be created for cleaner code seperation. 
courseController.routeCourses(api)


### MAIN
if __name__ == '__main__':
    app.run()