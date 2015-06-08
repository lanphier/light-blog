from .. import main
from flask import render_template, abort, request
from flask_login import login_required

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@login_required
@main.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':

    else:
        return render_template('create-post.html')
