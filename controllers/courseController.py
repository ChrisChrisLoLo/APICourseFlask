from models import courseModel
from flask_restful import Resource

class Course(Resource):
    def get(self):
        courses = courseModel.Course.query.all()
        return courses
    


def routeCourses(api):
    api.add_resource(Course, '/hi')