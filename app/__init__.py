from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_oauthlib.provider import OAuth2Provider
from flask import Flask
from config import config

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

oauth = OAuth2Provider()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    db.init_app(app)

    login_manager.init_app(app)

    oauth.init_app(app)

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    from .oauth import oauth_blueprint
    app.register_blueprint(oauth_blueprint)

    return app