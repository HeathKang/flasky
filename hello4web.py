from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask import Flask,render_template,url_for
from flask.ext.script import Manager

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name',validators=[Required()])
    submit = SubmitField('Submit')
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager=Manager(app)
bootstrap=Bootstrap(app) #创建示例并初始化
moment=Moment(app)

@app.route('/',methods=['GET','POST'])
def index():
    img = url_for('static',filename='favicon.ico')
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html',img=img,current_time=datetime.utcnow(),form=form,name=name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


if __name__ == '__main__':
   manager.run()


    
