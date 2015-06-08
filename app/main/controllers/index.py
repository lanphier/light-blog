from .. import main
from ..models.post import Post
from ..errors import PostError
from ..forms.create_post_form import CreatePostForm
from app import db
from flask import render_template, request, redirect
from flask_login import login_required, current_user

@main.route('/', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.create_time.desc()).all()
    return render_template('index.html', posts=posts)

@login_required
@main.route('/create-post', methods=['GET', 'POST'])
def create_post():
    response_error = {}
    if request.method == 'POST':
        create_post_form = CreatePostForm()
        if create_post_form.validate_on_submit():
            post = Post(title=create_post_form.title.data,
                        content=create_post_form.content.data,
                        user=current_user._get_current_object())
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        else:
            response_error['code'] = PostError.IllegalForm
            return render_template('create-post.html', error=response_error)
    else:
        return render_template('create-post.html')
