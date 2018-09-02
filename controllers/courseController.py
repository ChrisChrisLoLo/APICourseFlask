from models.courseModel import * 
from flask import jsonify, request

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
        VALID_QUERY_PARAMETERS = ('minCourseNum','maxCourseNum','subject','faculty','sortBy','sortOrder')
        for argument in request.args:
            print(argument)
            if argument not in VALID_QUERY_PARAMETERS:
                print('ERROR')
                return errorResponse(400,'Parameter \'{}\' is not a valid query parameter for the requested URL.'.format(argument))
        courses = Course.query.limit(5).all()
        #print(request.args)
        courses = courses_schema.dump(courses).data
        res = jsonify({'status': 200,'data': courses})
        return res, 200

#TODO: Make this function a decorator and utilize it if need be.
def validateQueryParameters(parameterSet):
    for argument in request.args:
        if argument not in parameterSet:
            return errorResponse(400,'Parameter \'{}\' is not a valid query parameter for the requested URL.'.format(argument))

def errorResponse(HTTPStatus,message):
    res = jsonify({'status':HTTPStatus,'message': message})
    return res, HTTPStatus