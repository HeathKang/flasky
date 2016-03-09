from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField,SubmitField,BooleanField,SelectField,SubmitField,TextAreaField
from wtforms.validators import Required,Length,Email,Regexp
from wtforms import ValidationError
from ..models import Role,User

class EditProfileForm(Form):
	name = StringField('Real Name',validators=[Length(0,64)])
	location = StringField('location',validators=[Length(0,64)])
	about_me = TextAreaField('About_me')
	submit = SubmitField('Submit')

class EditProfileAdminForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	username = StringField('Username',validators=[Required(),Length(1,64),
							Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
									'Usernames must have only letters,'
									'numbers,dots or underscores')])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role',coerce=int)
	name = StringField('Realname',validators=[Length(0, 64)])
	location = StringField('Location',validators=[Length(0, 64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')

	def __init__(self,user,*args,**kwargs):
		super(EditProfileAdminForm,self).__init__(*args,**kwargs)
		self.role.choices =[(role.id,role.name)
							for role in Role.query.order_by(Role.name).all()]
		self.user = user 

	def validate_email(self,field):
		if field.data != self.email and \
				User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self,field):
		if field.data != self.username and \
				User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

class PostForm(Form):
	body = PageDownField("What's on your mind?",validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(Form):
	body = StringField('',validators=[Required()])
	submit = SubmitField('submit')
	
