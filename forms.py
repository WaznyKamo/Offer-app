from flask_wtf import Form
from __init__ import db
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class UserForm(Form):
    first_name = StringField('First name: ', validators=[DataRequired(), Length(min=3, max=20)])
    last_name = StringField('Last name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])


class Login(Form):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
