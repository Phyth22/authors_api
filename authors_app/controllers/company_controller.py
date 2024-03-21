from flask import  Blueprint, request,jsonify

from authors_app.models.user import User
from authors_app.extension import db

auth = Blueprint('auth',__name__,url_prefix= '/api/v1/auth')

@auth.route('/register',methods =['POST'])  

def register():
    
    
    company_name = request.json['company_name']
    description = request.json['description']
    email = request.json['email']
    origin = request.json['origin']
    
    
   
    
    if not company_name:
        return jsonify({"error your company_name is required"})
    
    if not origin:
        return jsonify({"error your origin is required"})
    
    if not description:
        return jsonify({"error your description is required"})
    
    if not email:
        return jsonify({"error your email is required"})
    
    
    
    
    
    company= company(company_name=company_name, origin=origin, email=email, description=description)
    return jsonify({'message': 'company registered successfully'})