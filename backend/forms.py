
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=300)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class csrf_form(FlaskForm):
    submit = SubmitField('Submit')

class NoteForm(FlaskForm):
    note = TextAreaField('Note', validators = [DataRequired(), Length(min=1, max=800)])
    boolean = BooleanField('Boolean Field',  default="checked")
    float = FloatField('Float', validators = [DataRequired()])
    date = DateField('Date',default=date.today, validators = [DataRequired()])
    submit = SubmitField('Submit')
