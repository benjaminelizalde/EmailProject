from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template
from flask_mail import Mail, Message

import csv
import pprint
import os

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
    
    return render_template('Page3.html' , sent="msg1 sent")
    

@app.route('/next3',methods=["POST","GET"])
def rendernext3():

    session["message2"] = request.form['data']
    
    
    return render_template('Page4.html' , sent="msg2 sent")
    

@app.route('/next4',methods=["POST","GET"])
def rendernext4():
    
    session["message3"] = request.form['data']
    
    return render_template('Page5.html' , sent="msg3 sent")
    

@app.route('/next5',methods=["POST","GET"])
def rendernext5():
   
   session["message4"] = request.form['data']

    
   return render_template('Page6.html' , sent="msg4 sent")
    
    
@app.route('/next6',methods=["POST","GET"])
def rendernext6():
    
    session["message5"] = request.form['data'] + ',' + request.form['data1']
     
    messg = session['message1'] + ',' + session['message2'] + ',' + session['message3'] + ',' + session['message4'] + ',' + session['message5'] 
    msg = Message('User Dats', sender = 'codingbot@gmail.com', recipients = ['codingbot0@gmail.com'])
    msg.attach("data.csv", "data/csv" , messg )

    mail.send(msg)
    
    return render_template('Page7.html' , sent="msg5 sent")


if __name__ == '__main__':
    os.system("echo json(array) > file")
    app.run()