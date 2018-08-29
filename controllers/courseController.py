from models import courseModel
from flask_restful import Resource

class Course(Resource):
    def get(self):
        return 'HIIII'

def routeCourses(api):
    api.add_resource(Course, '/hi')