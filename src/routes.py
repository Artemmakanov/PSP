from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy import create_engine
from flask import current_app as app

import jwt
import datetime

from .db_models import Users
from .config import conf

engine = create_engine(conf.postgres_url)

def get_users():
    Session = sessionmaker(engine)
    with Session() as session:
        result = session.execute(select(Users))
    return result.all()


# Секретный ключ для подписи JWT
SECRET_KEY = 'your_secret_key'

# Функция для создания JWT
def create_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Токен действителен 1 час
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Функция для проверки JWT
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['username']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

# Эндпоинт для аутентификации
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    users = get_users()

    for user in users: 
        if user.name == username and user.password == password:
            token = create_token(username)
            return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

# Защищенный эндпоинт
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 403

    username = verify_token(token)
    if isinstance(username, str) and 'Token' in username:
        return jsonify({'message': username}), 403

    return jsonify({'message': f'Hello, {username}! This is a protected route.'})
