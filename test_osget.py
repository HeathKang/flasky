import os
print (os.environ)
filename = os.environ.get('MAIL_USERNAME')
print (filename)