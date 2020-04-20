from chat_app.models import User, Posts
from flask import request, render_template, redirect, flash, url_for
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
    return render_template('user_home.html') 


@app.route('/user_info', methods=['GET'])
def user_info_page():
    return render_template('user_info.html')


@app.route('/posts', methods=['GET'])
def posts():    
    return render_template('posts.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account create for {form.username.data}!', 'success')
        return redirect(url_for('user_page'))
    return render_template('register.html', form=form)

