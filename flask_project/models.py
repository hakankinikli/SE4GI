# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:43:03 2022

@author: hakan
"""
from flask_project import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Country(db.Model):
    countryname=db.Column(db.String(50),primary_key=True,unique=True,nullable=False)
    countrycode=db.Column(db.String(20),unique=True,nullable=False)
    
    def __repr__(self):
        return f"Country('{self.countryname}','{self.countrycode}')"
    
class City(db.Model):
    cityname=db.Column(db.String(50),primary_key=True,unique=True,nullable=False)
    citycode=db.Column(db.String(20),unique=True,nullable=False)
    countryname=db.Column(db.String(50),db.ForeignKey('country.countryname'),nullable=False)
    
    def __repr__(self):
        return f"City('{self.cityname}''{self.citycode}''{self.countryname}')"
    
    

class Poi(db.Model):
    __tablename__='attraction'
    querytab=db.Column(db.String(255),nullable=False)
    name=db.Column(db.String(50),primary_key=True,nullable=False)
    typee=db.Column(db.String(255),nullable=False)
    subtype=db.Column(db.String(255),nullable=False)
    category=db.Column(db.String(255),nullable=False)
    street=db.Column(db.String(255),nullable=False)
    city=db.Column(db.String(255),db.ForeignKey('City.cityname'),nullable=False)
    postal_code=db.Column(db.Integer(),nullable=False)
    state=db.Column(db.String(255),nullable=False)
    country=db.Column(db.String(255),nullable=False)
    country_code=db.Column(db.String(255),nullable=False)
    latitude=db.Column(db.Float(),nullable=False)
    longitude=db.Column(db.Float(),nullable=False)
    business_status=db.Column(db.String(255),nullable=False)
    description=db.Column(db.Text(),nullable=True)

    def __init__(self,name, typee, city, latitude,longitude):
        self.name=name     
        self.typee=typee
        self.city=city
        self.latitude=latitude
        self.longitude=longitude
        
    def __repr__(self):
        return f"<Place {self.name}>"
    

     
# # =============================================================================
# # class Post(db.Model):
# #     id = db.Column(db.Integer,primary_key=True)
# #     title=db.Column(db.String(100),nullable=True)
# #     date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
# #     content=db.Column(db.text,nullable=False)
# #     
# # =============================================================================
#     def __repr__(self):
#         return f"User('{self.title}',{self.date_posted})"
#     
# =============================================================================