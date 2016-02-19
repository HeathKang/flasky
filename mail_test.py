import os
from flask import Flask
from flask.ext.mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'xxxxxxxxx@qq.com'
app.config['MAIL_PASSWORD'] = 'xxxxxxxxxxxxxxxx'
mail = Mail(app)
            
@app.route('/')
def index():
    msg = Message('test',sender='xxxxxxxxx@qq.com',recipients=['heath.kang@foxmail.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    mail.send(msg)

    return 'ok'

if __name__ == '__main__':
	app.run(debug=True)

