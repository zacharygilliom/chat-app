from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120),  nullable=False)

    def __repr__(self):
        return f'User {self.id}'

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '{name: '+ self.firstname + ' ' + self.lastname + ', age:'+str(self.age)+ '}' 


@app.route('/')
def home_screen():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login_screen():
    return render_template('login.html')

@app.route('/user_home', methods=['GET', 'POST'])
def user_page():
    if request.method == 'POST':
        username = request.form['validationCustomUsername']
        password = request.form['exampleInputPassword1']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        # all_users = User.query.all()
    return render_template('user_home.html', username=username, password=password)

if __name__ == '__main__':
    app.run(debug=True)