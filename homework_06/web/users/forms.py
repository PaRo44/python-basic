from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email


class UserForm(FlaskForm):
    name = StringField('Name: ', validators=[InputRequired()])
    email = StringField('Email: ', validators=[InputRequired(), Email()])
    login = StringField('Login: ', validators=[InputRequired()])
    surname = StringField('Surname: ', validators=[InputRequired()])
    submit = SubmitField('Submit')
