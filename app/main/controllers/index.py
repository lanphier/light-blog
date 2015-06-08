from .. import main
from flask import render_template, abort, request

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
    elif request.method == 'GET':
    else:
