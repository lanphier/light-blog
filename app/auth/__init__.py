from flask import Blueprint

auth = Blueprint('auth', __name__)

from .controllers import login
from .controllers import register
