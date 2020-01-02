from flask_env import MetaFlaskEnv


class AppConfiguration(metaclass=MetaFlaskEnv):
    DEBUG = True
    POSTGRES_URI = 'xxx'
