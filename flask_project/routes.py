# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:27:15 2022

@author: hakan
"""
from flask import render_template, url_for, flash, redirect, request,Blueprint
from flask_project import app, db
from flask_project.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_project.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from flask_project.POI import add_map,add_marker,add_legend
from flask_project.server import connectToDB
import pandas as pd



users = Blueprint('users', __name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')
# =============================================================================
# @app.route("/discover")
# def viewmap():
#     return render_template("viewmap.html")
# 
# =============================================================================
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect('home')

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account',
                          form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password== form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/viewmap",methods=['GET','POST'])
def viewmap():
    # this is base map
    conn=connectToDB()
    
# =============================================================================
#     cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     try:
#         cur.execute("select querytab,name,site,city,street,latitude,longitude,description from attraction")
#     except:
#         print('Error executing select')
# =============================================================================
# =============================================================================
#     results=cur.fetchall()
#     results=pd.DataFrame(results)
# =============================================================================
    df= pd.read_sql("select querytab,name,site,city,street,latitude,longitude,description from attraction", con=conn)
    milanmap=add_map(45.47,9.16,'Stamen Terrain')
    markeredmap=add_marker(df,milanmap)
    maplegend=add_legend(markeredmap)

    return render_template('viewmap.html', map=maplegend._repr_html_(),title='Discover')

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password=form.password
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.password=current_user.pasword
    return render_template('account.html', title='Account',
                          form=form)



