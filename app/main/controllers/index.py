from .. import main_blueprint

@main_blueprint.route('/index', methods=['GET'])
def index():
    return 'index'