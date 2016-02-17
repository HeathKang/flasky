from flask import Flask
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.mail import Message
from threading import Thread

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <xxxxxxxxxxg@foxmail.com>'
app.config['MAIL_SEVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'xxxxxxxxxx@foxmail.com'
app.config['MAIL_PASSWORD'] = 'xxxxxxxx'
app.config['FLASKY_ADMIN'] = 'xxxxxxxxxxx@foxmail.com'

app = Flask(__name__)
app.config.from_object(__name__)

mail = Mail(app)

def send_async_email(app,msg):

    with app.app_context():
            mail.send(msg)
            
def SendMail():

    msg = Message('test',sender='heath.kang@foxmail.com',recipients=['xxxxxxxxxxx@qq.com'])
    msg.body = "text body"
    msg.html = "<b>HTML</b>body"
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return "OK"