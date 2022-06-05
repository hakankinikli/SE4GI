# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:23:35 2022

@author: hakan
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY']='2550ed47c3c8e9c5c05872d4ac1719c3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://hkpostgres:postgres@localhost:5432/hkflaskapp"

db = SQLAlchemy(app)
fbcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flask_project import routes 