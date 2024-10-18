import jwt
import datetime
from flask import current_app

def create_access_token(username):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    return jwt.encode({'sub': username, 'exp': expiration}, current_app.config['SECRET_KEY'], algorithm='HS256')

def create_refresh_token(username):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    return jwt.encode({'sub': username, 'exp': expiration}, current_app.config['SECRET_KEY'], algorithm='HS256')

