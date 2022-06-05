# -*- coding: utf-8 -*-
"""
Created on Sun May 29 21:40:04 2022

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:27:15 2022

@author: hakan
"""
from flask import render_template, url_for, flash, redirect, request
from flask_project import app, db, fbcrypt
from flask_project.forms import RegistrationForm, LoginForm
from flask_project.models import User
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]





@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/discover")
def viewmap():
    return render_template("viewmap.html",title="Discover")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = fbcrypt.generate_password_hash(form.password.data.encode('utf-8'))
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and fbcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)