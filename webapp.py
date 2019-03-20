from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template
from flask_mail import Mail, Message
from time import localtime, strftime

import csv
import pprint
import os
import random


app = Flask(__name__)

app.debug = True #Change this to False for production
app.secret_key = os.environ['SECRET_KEY'] #used to sign session cookies


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'codingbot0@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/')
def Page1():
    
    print(strftime("%a %d %b %Y %H:%M:%S", localtime()))
    for i in range(20):
        print(random.randint(10000,99999))
    

    
    return render_template('Page1.html')
    

    
@app.route('/page2')
def Page2():
    return render_template('Page2.html')
    
    
@app.route('/page3')
def Page3():
    return render_template('Page3.html')
    
    
@app.route('/next1',methods=["POST","GET"])
def rendernext1():
    #messg = request.form['data']
    return render_template('Page2.html')


@app.route('/next2',methods=["POST","GET"])
def rendernext2():
    
    session["message1"] = request.form['data']
    
    return render_template('Page3.html' )
    

@app.route('/next3',methods=["POST","GET"])
def rendernext3():

    session["message2"] = request.form['data']
    
    
    return render_template('Page4.html' )
    

@app.route('/next4',methods=["POST","GET"])
def rendernext4():
    
    session["message3"] = request.form['data']
    
    return render_template('Page5.html' ,msg3=session["message3"])
    

@app.route('/next5',methods=["POST","GET"])
def rendernext5():
   
   session["message4"] = request.form['data']

    
   return render_template('Page6.html' ,msg4= session["message4"])
    
    
@app.route('/next6',methods=["POST","GET"])
def rendernext6():
    math = ['murphy','phelps','ruissner']
    english = ['slemp','light','nye']
    history = ['tormey','mendoza','jackson']
    s = ['cadenasso','poster','quinn']
    for i in range(1):
        session["math"] = random.choice(math)
        session["english"] = random.choice(english)
        session["history"] = random.choice(history)
        session["science"] = random.choice(s)
    for i in range(20):
        session["code1"]=(random.randint(10000,99999))
        session["code2"]=(random.randint(10000,99999))
        session["code3"]=(random.randint(10000,99999))
        session["code4"]=(random.randint(10000,99999))
    session["message5"] = request.form['data'] + ',' + request.form['data1'] + ',' + request.form['data2'] + ',' + strftime("%a %d %b %Y %H:%M:%S", localtime())
    
    messg = 'Math' + ',' + 'English' + ',' + 'History' + ',' + 'Science' + ',' + 'Weighted GPA' + ',' + "Unweighted GPA" + ',' + "Student ID" + ',' + "Time Sent" + "\n" + session['message1'] + ',' + session['message2'] + ',' + session['message3'] + ',' + session['message4'] + ',' + session['message5']
    msg = Message('User Dats', sender = 'codingbot@gmail.com', recipients = ['codingbot0@gmail.com'])
    msg.attach("data.csv", "data/csv" , messg)

    mail.send(msg)
    
    return render_template('Page7.html' , math = session["math"], english = session["english"], history = session["history"], science = session["science"], code1 = session["code1"] , code2 = session["code2"] , code3 = session["code3"] , code4 = session["code4"] ,msg1=session["message1"], msg2= session["message2"],  msg3= session["message3"],  msg4= session["message4"],  time=strftime("%a, %d %b %Y %H:%M:%S ",localtime()))
    


if __name__ == '__main__':
    os.system("echo json(array) > file")
    app.run()