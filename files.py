from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Match me!')

class MatchForm(FlaskForm):
    again = SubmitField('Match Again')
    exit = SubmitField('Exit')