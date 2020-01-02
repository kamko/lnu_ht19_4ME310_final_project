from flask_env import MetaFlaskEnv


class AppConfiguration(metaclass=MetaFlaskEnv):
    DEBUG = True
    ADMIN_ACCESS_TOKEN = 'lalalal'
    SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\j\projects\adaptive-web-project\blog\be\db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
