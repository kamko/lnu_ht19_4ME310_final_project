import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_cors import CORS

from server import views
from server.config import AppConfiguration
from server.db import db
from server.serialization import ma
from server.service.popularity import check_new_articles


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfiguration)

    register_plugins(app)
    register_blueprints(app)

    schedule_job(app)

    return app


def register_blueprints(app):
    app.register_blueprint(views.root, url_prefix='/')
    app.register_blueprint(views.admin, url_prefix='/admin')
    app.register_blueprint(views.article, url_prefix='/article')


def register_plugins(app):
    CORS(app)
    db.init_app(app)
    ma.init_app(app)


def schedule_job(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: check_new_articles(app), trigger="interval",
                      seconds=AppConfiguration.PREDICTION_CHECK_INTERVAL)
    print("scheduler - start")
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())
