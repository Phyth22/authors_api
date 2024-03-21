from authors_app import db
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from authors_app.extension import db




class User(db.Model):
    __tablename__="users"
     # Attributes of the User and their respective constraints  
    id = db.Column(db.Integer,primary_key= True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    contact  =db.Column(db.String(255), nullable=False,unique=True)
    image=db.Column(db.String(255), nullable=False )
    user_type = db.Column(db.String(255),nullable=False)
    biography= db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255), nullable=False , unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now())  
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
        
   
   
def __init__(self, first_name, last_name, email, contact, password_hash,  user_type, biography,image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password_hash = password_hash
        self.biography = biography
        self.user_type = user_type
        self.image = image
        
        
def get_full_name(self):  
        return "{self.last_name}{self.first_name}"

