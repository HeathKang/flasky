from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email

class LoginForm(Form):
    email = StringField('email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('password',validators=[Required()]) #表单填写
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')

