from email import message
from flask import Flask,render_template,redirect,url_for,Request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG']= True
app.config['TESTING']= False
app.config['MAIL_SERVER']= 'gsmtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'sudheerkumarseera777@gmail.com'
app.config['MAIL_PASSWORD'] = 'Sudheer@23'
app.config['MAIL_DEFAULT_SENDER'] = 'sudheerkumarseera777@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    msg = Message('subject Line',sender='sudheerkumarseera777@gmail.com',recipients=['sudheer.edu.feb@gmail.com'])
    mail.send(msg)
    return "success"

if __name__ =='__main__':
    app.run(debug =True)