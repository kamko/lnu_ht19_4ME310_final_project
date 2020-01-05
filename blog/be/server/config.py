from flask_env import MetaFlaskEnv


class AppConfiguration(metaclass=MetaFlaskEnv):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\j\projects\adaptive-web-project\blog\be\db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PREDICTION_CHECK_INTERVAL = 30
    ITEMS_PER_PAGE = 20
