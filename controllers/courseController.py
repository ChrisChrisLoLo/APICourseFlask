from models.courseModel import * 
from flask_restful import Resource

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)



class CourseResource(Resource):
    def get(self):
        #courses = Course.query.get(2)
        courses = Course.query.all()
        print(courses)
        courses = courses_schema.dump(courses).data
        return {'status': 'success','data': courses},200


def routeCourses(api):
    api.add_resource(CourseResource, '/hi')