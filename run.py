import os

from app import create_app
from app.config import app_config
from controllers import courseController


### INITIALIZATION
# Initialize the flask app,api,db, and any commands
app,api = create_app()

### ROUTING
# The routing will occur in run.py for now. A new routing file may need to
# be created for cleaner code seperation. 
courseController.routeCourses(api)


### MAIN
if __name__ == '__main__':
    app.run()