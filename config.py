import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kaopuchou'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(self):
        pass

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

config = {
    'dev': DevConfig(),
    'prod': ProdConfig(),
    'default': DevConfig()
}