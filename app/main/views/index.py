from .. import main

@main.route('/index', methods=['GET'])
def index():
    return 'index'