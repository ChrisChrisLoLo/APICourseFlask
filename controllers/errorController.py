from flask import jsonify

def routeErrors(app):
    @app.errorhandler(405)
    def methodNotAllowed(e):
        res = {'status':405,
                'message':'The HTTP method is not allowed for the requested URL.'
        }
        return jsonify(res), 405