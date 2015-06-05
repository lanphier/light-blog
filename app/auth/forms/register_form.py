from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(validators=[DataRequired()])