from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

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

    def __init__(self, username, email, tel):
        self.username = username
        self.email = email
        self.tel = tel

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

        insertUser = Employee(username, email, tel)
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
        db.session.commit()

        return redirect(url_for('index'))