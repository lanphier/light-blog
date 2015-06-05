from .. import main

@main.route('/index', method=['GET'])
def main():
    return 'index'