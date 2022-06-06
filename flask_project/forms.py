# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:02:36 2022

@author: hakan
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_project.models import User

class RegistrationForm(FlaskForm):
    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                           validators=[DataRequired()]) 
    confirm_password=PasswordField(' Confirm Password',
                           validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    
    
    
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That user name is taken. Please choose a different one!')
            
    def validate_email(self,email):
        if email.data != current_user.email:
            email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one!')
    
class LoginForm(FlaskForm):
# =============================================================================
#     username=StringField('Username',
#                          validators=[DataRequired(),Length(min=2,max=20)])
# =============================================================================
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                           validators=[DataRequired()]   ) 
# =============================================================================
#     confirm_password=PasswordField(' Confirm Password',
#                            validators=[DataRequired(),EqualTo('password')]   )
# =============================================================================
    remember=  BooleanField('Remember Me ')  
    submit=SubmitField('Login')
    
    
class UpdateAccountForm(FlaskForm):
    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jpeg','png'])])
    
    submit=SubmitField('Update')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That user name is taken. Please choose a different one!')
            
    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one!')