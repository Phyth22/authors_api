
# from datetime import datetime
# from authors_app.extension import db
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy




# class Company(db.Model):
#     __tablename__="Companies"     
#     # Attributes of the User and their respective constraints  
#     id = db.Column(db.Integer,primary_key= True)
#     company_name = db.Column(db.String(100),unique=True)
#     origin = db.Column(db.String(100),nullable=False)
#     description = db.Column(db.Text(100),nullable =False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship('user',backref='Companies')
#     created_at = db.Column(db.DateTime, default=datetime.now())  
#     updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
#     # adding a constructor for the company class
#     def __init__(self,name,origin,description,user_id):
#         self.name = name
#         self.description = description
#         self.user_id = user_id
#         self.origin = origin
        
        
        
#     def __repr__(self):  
#         return "{self.name}{self.origin}"
    



from datetime import datetime
from authors_app.extension import db
from flask_sqlalchemy import SQLAlchemy

class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), unique=True)
    origin = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='companies')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    

    def __init__(self, company_name, origin, description, user_id):
        self.company_name = company_name
        self.origin = origin
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f"{self.company_name} - {self.origin}"
