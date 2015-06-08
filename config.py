import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kaopuchou'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:nebula@127.0.0.1:5432/light-blog'

    WTF_CSRF_ENABLED = False
    WTF_CSRF_CHECK_DEFAULT = False

    OAUTH2_PROVIDER_ERROR_URI = '/oauth/errors'
    OAUTH2_PROVIDER_TOKEN_EXPIRES_IN = 3600

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