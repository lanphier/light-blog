from .. import auth_blueprint
from ..forms.login_form import LoginForm
from ..models.user import User
from flask import redirect, url_for
from flask_login import login_user, logout_user, login_required

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, True)
            return redirect(url_for('main.index'))
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))