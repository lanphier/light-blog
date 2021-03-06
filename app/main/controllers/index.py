from .. import main
from ..models.post import Post
from ..errors import PostError
from ..forms.create_post_form import CreatePostForm
from app import db
from flask import render_template, request, redirect
from flask.ext.login import login_required, current_user

@main.route('/', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.create_time.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    response_error = {}
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(title=form.title.data,
                        content=form.content.data,
                        user=current_user._get_current_object())
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        else:
            response_error['code'] = PostError.IllegalForm
            return render_template('create-post.html', error=response_error)
    else:
        return render_template('create-post.html', form=form, error=response_error)
