from flask import Flask,render_template,request,redirect,url_for
from flask import Flask
import mysql.connector as c
import database as db

app = Flask(__name__)
   
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        data1 = db.show1() 
        email_li = []
        for i in data1:
            s = i[0]
            s = str(s)
            if('\xa0' in s):
                s = s.replace(u'\xa0', u' ')
                email_li.append(s[1:])
            else:
                email_li.append(s)
        print(email_li)
        return render_template("output1.html",mails = email_li)
    
    elif request.method == 'POST':
        per = request.form['year']
        data = db.showResult(per)        
        return render_template('table.html',table = data)


if __name__ =='__main__':
    app.run(port =5000,debug =True)
