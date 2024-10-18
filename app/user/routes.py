import jwt
from flask import Blueprint, request, jsonify
from app.user.models import register_user,login_user,change_password,delete_user
from app.utils import create_access_token,create_refresh_token,current_app

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    try:
        user_data = request.json
        user = register_user(user_data['username'], user_data['password'])
        return jsonify(user), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500 

@user_bp.route('/login', methods=['POST'])
def login():
    user_data = request.json
    if login_user(user_data['username'], user_data['password']):
        access_token = create_access_token(user_data['username'])
        refresh_token = create_refresh_token(user_data['username'])

        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "Login successful",
            "status": 200
        }), 200
    return jsonify({"message": "Invalid credentials", "status": 401}), 401

@user_bp.route('/change-password', methods=['POST'])
def change_password_route():
    try:
        user_data = request.json
        print('user_data::::',user_data)
        result = change_password(user_data['username'], user_data['old_password'], user_data['new_password'])
        return jsonify(result), result['status']
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
@user_bp.route('/delete-user', methods=['DELETE'])
def delete_user_route():
    try:
        user_data = request.json
        result = delete_user(user_data['username'])
        return jsonify(result), result['status']
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    
@user_bp.route('/refresh-token', methods=['POST'])
def refresh_token():
    refresh_token = request.json.get('refresh_token')
    try:
        payload = jwt.decode(refresh_token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        username = payload['sub']
        new_access_token = create_access_token(username)
        return jsonify({
            "access_token": new_access_token,
            "message": "Token refreshed successfully",
            "status": 200
        }), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Refresh token has expired", "status": 401}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid refresh token", "status": 401}), 401