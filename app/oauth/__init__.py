from flask import Blueprint

oauth_blueprint = Blueprint('oauth', __name__)

from .controllers import authorize