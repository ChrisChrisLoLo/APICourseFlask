from models import courseModel
from flask_restful import Resource

class Course(Resource):
    def get(self):
        courses = courseModel.Course.query.all()
        courseNames = []
        for course in courses:
            courseNames.append(course.name)
        return courseNames
    


def routeCourses(api):
    api.add_resource(Course, '/hi')