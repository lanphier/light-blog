from .. import auth
from ..forms.login_form import LoginForm
from ..models.user import User
from ..errors import UserError
from flask import redirect, url_for, request, render_template
from flask_login import login_user, logout_user, login_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
    response_error = {}
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None:
                if user.verify_password(form.password.data):
                    login_user(user, True)
                    return redirect(url_for('main.index'))
                else:
                    response_error['code'] = UserError.WrongPassword
            else:
                response_error['code'] = UserError.UserNotExist
        else:
            response_error['code'] = UserError.IllegalForm
        return render_template('login.html', error=response_error)
    else:
        return render_template('login.html', error=response_error)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))