
from flask import Blueprint, url_for
from flask_restplus import Api


api_bp = Blueprint('api', __name__)


class CustomApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = 'http' if '5000' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


swagger_doc = '/' if os.environ.get('ENV_MODE', '').upper() != 'PROD' else ''

api = CustomApi(
    app=api_bp,
    version='1.0',
    title='Page builder API',
    validate=False,
    doc=swagger_doc  # disable Swagger UIs
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """

    from.file_convert import file_convert_ns
    app.register_blueprint(api_bp)
    api.add_namespace(file_convert_ns)


from . import requests
from . import responses
