from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(validators=[DataRequired()])