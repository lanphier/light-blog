from .. import main
from ..models.post import Post
from ..errors import PostError
from ..forms.create_post_form import CreatePostForm
from flask import render_template, abort, request
from flask_login import login_required, current_user

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@login_required
@main.route('/create-post', methods=['GET', 'POST'])
def create_post():
    response_error = {}
    if request.method == 'POST':
        create_post_form = CreatePostForm()
        if create_post_form.validate_on_submit():
            post = Post(title=create_post_form.title.data,
                        content=create_post_form.content.data)
        else:
            response_error['code'] = PostError.IllegalForm
    else:
        return render_template('create-post.html')
