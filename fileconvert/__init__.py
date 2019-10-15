
import flask
# import re
# from fileconvert.extensions import redis as _redis, exceptions as exct
# from util import auth

__author__ = 'HuanPL'


def _after_request(response):
    

    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers[
        'Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers[
        'Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'

    return response


def _before_request():
    """

    :return:
    """



def create_app():
    from fileconvert import api, models

    app = flask.Flask(__name__)

    app.before_request(_before_request)
    app.after_request(_after_request)

    # sub-modules initialization
    models.init_app(app)
    api.init_app(app)
    return app


# redis = _redis.make_redis()
app = create_app()