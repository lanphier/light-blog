import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kaopuchou'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:19910108@127.0.0.1:5432/light-blog'

    WTF_CSRF_ENABLED = True
    WTF_CSRF_CHECK_DEFAULT = True
    WTF_CSRF_TIME_LIMIT = 1800

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