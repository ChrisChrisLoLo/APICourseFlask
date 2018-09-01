from models.courseModel import * 
from flask import jsonify

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

def routeCourses(app):
    """
    Add any routes to the Flask app that pertain to
    the Course model. 
    """
    #api.add_resource(CourseResource, '/courses')
    @app.route('/courses',methods=['GET'])
    def getCourses():
        courses = Course.query.limit(5).all()
        print(courses)
        courses = courses_schema.dump(courses).data
        res = jsonify({'status': 200,'data': courses})
        return res, 200
