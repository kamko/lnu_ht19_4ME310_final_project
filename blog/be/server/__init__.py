from flask import Flask
from flask_cors import CORS

from server import views
from server.config import AppConfiguration


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfiguration)

    register_plugins(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(views.root, url_prefix='/')
    app.register_blueprint(views.admin, url_prefix='/admin')
    app.register_blueprint(views.article, url_prefix='/article')


def register_plugins(app):
    CORS(app)
