# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:50:38 2022

@author: hakan
"""

from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'