from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import Flask
from config import config

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.template_folder = 'templates'
    app.debug = True

    config[config_name].init_app(app)

    db.init_app(app)

    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app