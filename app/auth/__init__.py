from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

from .controllers import login
from .controllers import register

