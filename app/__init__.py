from flask import Flask, make_response, jsonify
from flask_cors import CORS


def create_app(test_config=None,):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,template_folder='templates')
    CORS(app)


    from app.api import render

    app.register_blueprint(render.bp)


    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify(error='Not found'), 400)

    @app.errorhandler(500)
    def error_500(error):
        return make_response({}, 500)

    return app
