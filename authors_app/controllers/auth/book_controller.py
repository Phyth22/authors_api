from flask import  Blueprint, request,jsonify

from authors_app.models.user import User
from authors_app.extension import db

auth = Blueprint('auth',__name__,url_prefix= '/api/v1/auth')

@auth.route('/register',methods =['POST'])  

def register():
    
    
    title = title.json['title']
    description = description.json['description']
    image = image.json['image']
    price = price.json['price']
    price_unit = price_unit.json['price_unit']
    pages =pages.json['pages']
    publication_date = publication_date.json['publication_date']
    image = request.json['image']
    genre = genre.json['genre']
    isbn = isbn.json['isbn']
    user= user.json['user']
     
    
   
    
    if not title:
        return jsonify({"error your title is required"})
    
    if not description:
        return jsonify({"error your description is required"})
    
    if not image:
        return jsonify({"error your email is required"})
    
    if not price:
        return jsonify({"error your price is required"})
    
    if not price_unit:
        return jsonify({"error your price_unit is required"})
    
    if not pages:
        return jsonify({"error your pages is required"})
    
    if not publication_date:
        return jsonify({"error your publication_date is required"})
    
    if not genre:
        return jsonify({"error your genre is required"})
    
    if not isbn:
        return jsonify({"error your isbn is required"})
    
    if not book :
        return jsonify({"error your user is required"})
    
    
    
    
    
    
    
    book = book(title=title, description=description, price=price, genre=genre, publication_date=publication_date, isbn=isbn , pages=pages,)
    return jsonify({'message': 'book registered successfully'})