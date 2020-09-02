# -*- coding: utf-8 -*-
<<<<<<< HEAD
from gtts import gTTS
from playsound import playsound
=======
<<<<<<< HEAD
=======
from gtts import gTTS
from playsound import playsound
>>>>>>> 4c394300fb2843c913d7f3ed12dde659d8d0f300
>>>>>>> a852d1349b816a90e161e504668ccb130fa874ea
from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
encoding = 'ISO-8859-1'

app= Flask(__name__)
app.secret_key="Secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    userid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))
    jicw = db.Column(db.String(100))

    def __init__(self, username, email, tel,jicw):
        self.username = username
        self.email = email
        self.tel = tel
        self.jicw = jicw

@app.route("/")
def index():
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
    return render_template('index.html', employees=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']
        jicw = request.form['jicw']

        insertUser = Employee(username, email, tel,jicw)
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))
@app.route("/delete/<uid>")
def delete(uid):
    delUser = Employee.query.get(uid) #select * from Employee where userid=3
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateuser = Employee.query.get(request.form.get('userid'))
        updateuser.username = request.form['username']
        updateuser.email = request.form['email']
        updateuser.tel = request.form['tel']
        updateuser.jicw = request.form['jicw']
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchuser = Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template('index.html', employees=searchuser,txtsearch = txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "안녕하세요."
    filename = "hellosmartcat.mp3"
    tts = gTTS(text = text, lang="ko")
    tts.save(filename)
    playsound(filename)
    return "aaaa"
