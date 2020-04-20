from chat_app.models import User, Posts
from flask import request, render_template, redirect
from chat_app.forms import RegistrationForm, LoginForm
from chat_app import app
from chat_app import db



@app.route('/')
def home_screen():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/user_home', methods=['GET', 'POST'])
def user_page():
    if request.method == 'POST':
        db.create_all()
        username = request.form['validationCustomUsername']
        password = request.form['exampleInputPassword1']
        firstname = request.form['userFirstName']
        lastname = request.form['userLastName']
        new_user = User(username=username, password=password, firstname=firstname, lastname=lastname)
        db.session.add(new_user)
        db.session.commit()
    return render_template('user_home.html', username=username, password=password)


@app.route('/user_info', methods=['GET'])
def user_info_page():
    return render_template('user_info.html')


@app.route('/posts', methods=['GET'])
def posts():    
    return render_template('posts.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

