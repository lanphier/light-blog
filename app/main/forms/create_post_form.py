from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CreatePostForm(Form):
    title = StringField(validators=[DataRequired(), Length(1, 200)])
    content = StringField(validators=[DataRequired(), Length(1, 1000)])