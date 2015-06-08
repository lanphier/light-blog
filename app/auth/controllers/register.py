from .. import auth
from ..forms.register_form import RegisterForm
from ..models.user import User
from ..errors import UserError
from app import db
from flask import redirect, url_for, request, render_template, abort

@auth.route('/register', methods=['GET', 'POST'])
def register():
    response_data = {}
    response_error = {}
    if request.method == 'POST':
        form = RegisterForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None:
                user = User(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.index'))
            else:
                response_error['code'] = UserError.UserNotExist
        else:
            response_error['code'] = UserError.IllegalForm
        if not response_error:
            response_data['error'] = response_error
        return render_template('register.html', data=response_data)
    elif request.method == 'GET':
        return render_template('register.html', data=response_data)
    abort(403)