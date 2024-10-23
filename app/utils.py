import jwt
import datetime
from flask import current_app
import redis
from flask import request, jsonify
from functools import wraps

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def create_access_token(username):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    return jwt.encode({'sub': username, 'exp': expiration}, current_app.config['SECRET_KEY'], algorithm='HS256')

def create_refresh_token(username):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    refresh_token = jwt.encode({'sub': username, 'exp': expiration}, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    # Lưu refresh token vào Redis với thời gian hết hạn
    redis_client.setex(f'{username}', 30 * 24 * 60 * 60, refresh_token)  # 30 ngày

    return refresh_token

def check_refresh_token(username):
    # Lấy giá trị từ Redis
    token = redis_client.get(f'{username}')
    
    if token:
        return print("refresh_token::::::::",token.decode('utf-8'))
    else:
        return None  

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        token = token.split(" ")[1]
        print("token::::::",token)
        verification_result = verify_token(token)
        if verification_result == "expired":
            return jsonify({'message': 'Token has expired! Please refresh your token.', "status": 401}), 401
        elif verification_result == "invalid":
            return jsonify({'message': 'Token is invalid!'}), 403
        
        return f(*args, **kwargs)
    return decorated

def verify_token(token):
    try:
        decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return decoded  
    except jwt.ExpiredSignatureError:
        return "expired"
    except jwt.InvalidTokenError:
        return "invalid"

