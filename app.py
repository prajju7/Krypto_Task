from flask import Flask, render_template, redirect, url_for, request
import mysql
import mysql.connector
import flask_login as fl
from urllib.request import urlopen
import json
import smtplib

app = Flask(__name__)

# @app.route('/')
# def index():
#     #return app.make_response("Hello Prajwal Reddy")
#     return render_template("login.html")

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        if(authenticate(request.form['username'],request.form['password'])):
            app.make_response("Successully Logged In")
            #fl.login_user(request.form['username'], remember=True)
            return redirect(url_for('home_log',data= request.form['username']))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
us = ""
def authenticate(un,pa):
    us = un
    mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Prajwal@855")
    mycursor = mydb.cursor()
    s = "SELECT u_pass FROM krypto.userdata where u_name = \""+un+"\";"  #and u_pass = \""+ pa+"\";"
    mycursor.execute(s)
    myresult = mycursor.fetchall()
    if(len(myresult)>0 and pa==myresult[0][0]):
        return True
    return False

@app.route('/main')
def home_log():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = urlopen(url)
    data_json = json.loads(response.read())

    mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Prajwal@855")
    mycursor = mydb.cursor()

    us = request.args.get('data', None)
    print(us)
    s = "SELECT alerts,email FROM krypto.userdata where u_name = \""+us+"\";"  #and u_pass = \""+ pa+"\";"
    mycursor.execute(s)
    myresult = mycursor.fetchall()
    print(myresult)
    ap = myresult[0][0]
    ap = json.loads(ap)
    ap = ap["BTC"]
    em = myresult[0][1]
    cp = data_json[0]["current_price"]
    print(ap,em,cp)
    if(ap<=cp):
        sendMail("Price Crossed the Limit!!!",em)
         
    return render_template('Home.html')

def sendMail(s,e):
    s_e = "nirupreddy02102000@gmail.com"
    p = "Prajwalreddy"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(s_e,p)
    server.sendmail(s_e,e,s)
    print("SUCCESS")
    return
