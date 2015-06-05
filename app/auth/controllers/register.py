from .. import auth_blueprint
from ..forms.register_form import RegisterForm
from ..models.user import User
from app import db
from flask import redirect, url_for

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return redirect(url_for('main.index'))