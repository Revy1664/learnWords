from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class LoginForm(FlaskForm):

	username = StringField("username")
	password = PasswordField("password")


class RegistrationForm(FlaskForm):

	username = StringField("username")
	email = StringField("email")
	password = PasswordField("password")


class CardForm(FlaskForm):

	word = StringField("word")
	context = StringField("context")
