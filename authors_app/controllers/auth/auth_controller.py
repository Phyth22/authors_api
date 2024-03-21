from flask import Blueprint, request, jsonify
from authors_app.models.user import User
from flask_bcrypt import generate_password_hash, check_password_hash
from authors_app import db
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        contact = data.get('contact')
        user_type = data.get('user_type')
        password = data.get('password')
        biography = data.get('biography', '')
        image = data.get('image')

        # Input validation
        if not all([first_name, last_name, email, contact, user_type, password, image]):
            return jsonify({"error": "All fields are required"}), 400

        if len(password) < 8:
            return jsonify({"error": "Password should have 8 or more characters"}), 400

        if user_type == 'author' and not biography:
            return jsonify({"error": "Biography is required for authors"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 400

        if User.query.filter_by(contact=contact).first():
            return jsonify({"error": "Contact already exists"}), 400

        hashed_password = generate_password_hash(password)

        new_user = User(first_name=first_name, last_name=last_name, email=email, contact=contact,
                        password=hashed_password, user_type=user_type, biography=biography, image=image)

        db.session.add(new_user)
        db.session.commit()

        username = new_user.get_full_name()
        response_data = {
            'message': f'{username} has been successfully created as an {new_user.user_type}',
            'user': {
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
                'contact': new_user.contact,
                'type': new_user.user_type,
                'created_at': new_user.created_at,
            }
        }
        return jsonify(response_data), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({'error': 'Missing email or password'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid email or password'}), 401

        # Generate JWT token
        access_token = create_access_token(identity=user.id)

        return jsonify({'access_token': access_token}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        user_list = [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'contact': user.contact,
            'user_type': user.user_type,
            'biography': user.biography,
            'image': user.image,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        } for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.json
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.contact = data.get('contact', user.contact)
        user.user_type = data.get('user_type', user.user_type)
        user.biography = data.get('biography', user.biography)
        user.image = data.get('image', user.image)

        db.session.commit()

        return jsonify({'message': 'User updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


