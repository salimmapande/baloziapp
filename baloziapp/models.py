from enum import unique
from flask.app import Flask
from sqlalchemy.orm import relationship
from wtforms.fields.simple import TelField
from wtforms.validators import Length
from tamisemisystem import db#, login_manager
from flask_bcrypt import bcrypt
from flask_login import UserMixin
from alembic import op


#@login_manager.user_loader
#def load_user(user_id):
    #return User.query.get(user_id)


""" class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50),nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def  password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password) """


class Balozi(db.Model):
    __tablename__ = 'balozi'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable = False)
    surname = db.Column(db.String(length=50), nullable = False)
    nida = db.Column(db.String(length=30), nullable =False)
    street = db.Column(db.String(length=50), nullable = False)
    neighborhood = db.Column(db.String(length=50), nullable = False)#kitongoji
    county =  db.Column(db.String(length=50), nullable=False) #kata
    district_id = db.Column(db.Integer(), db.ForeignKey('district.id'))#wilaya
    district = db.Column(db.String(), nullable=False)
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'))#Mkoa
    region = db.Column(db.String(length=50), nullable=False)
    phonenumber = db.Column(db.String(length=15), nullable = True)



class District(db.Model):
    __tablename__ = 'district'
    id = db.Column(db.Integer(), primary_key=True)
    districtname = db.Column(db.String(length=50), nullable = False)
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'))
    #region = relationship('Region', back_populates='district')



class Region(db.Model):
    __tablename__ = 'region'
    id = db.Column(db.Integer(), primary_key=True)
    regionname = db.Column(db.String(length=50), nullable = False)



   
  
   


    
