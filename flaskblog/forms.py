from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,  IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    username = StringField('Orion ID', validators=[DataRequired()])
    password = PasswordField('Orion Password', validators=[DataRequired()])
    request_id = StringField('Request ID', validators=[Regexp(r'\d{8}')])
    submit = SubmitField('Continue')


#class OrionForm(FlaskForm):
#
#    username = StringField('Orion ID', validators=[DataRequired()])
#    password = PasswordField('Orion Password', validators=[DataRequired()])
#    submit = SubmitField('Logon Orion')