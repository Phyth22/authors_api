# # import statements
# from datetime import datetime
# from authors_app.extension import db
# from flask import Flask 

# class Book(db.Model):
#     __tablename__ = "books"  
    
#     # defining attributes for the book model
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150), nullable=False)
#     description = db.Column(db.String(255),nullable=False)
#     image = db.Column(db.String(255),nullable=True)
#     price = db.Column(db.Integer, nullable=False)
#     price_unit = db.Column(db.String(100),nullable=False,default='UGX')
#     pages = db.Column(db.Integer, nullable=False)
#     publication_date = db.Column(db.Date,nullable=False)
#     isbn = db.Column(db.String(150),nullable=False, unique=True)
#     genre = db.Column(db.String(50),nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user =db.relationship('user',backref='books') 
#     company_id = db.Column(db.Integer, db.ForeignKey('Companies.id')) 
#     created_at = db.Column(db.DateTime, default=datetime.now())  
#     updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
#     #adding a constructor for the book class
#     def __init__(self, title, price, description, user_id, genre, pages, publication_date, isbn):
#         super().__init__()
#         self.title = title
#         self.price = price
#         self.description = description
#         self.user_id = user_id
#         self.genre = genre
#         self.pages = pages
#         self.publication_date = publication_date
#         self.isbn = isbn
        
        
        
        
from datetime import datetime
from authors_app.extension import db
from flask import Flask

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    price_unit = db.Column(db.String(100), nullable=False, default='UGX')
    pages = db.Column(db.Integer, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(150), nullable=False, unique=True)
    genre = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='books')
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, title, price, description, user_id, genre, pages, publication_date, isbn):
        self.title = title
        self.price = price
        self.description = description
        self.user_id = user_id
        self.genre = genre
        self.pages = pages
        self.publication_date = publication_date
        self.isbn = isbn

    def __repr__(self):
        return f"{self.title} - {self.genre}"


        
        
    