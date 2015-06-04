from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    return 'login'

@auth.route('/register', methods=['GET'])
def register():
    return 'register'