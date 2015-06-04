from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    return 'index'