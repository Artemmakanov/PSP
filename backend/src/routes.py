from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy import create_engine
from flask import current_app as app

import hashlib
import jwt
import datetime

from .db_models import Users
from .config import conf

engine = create_engine(conf.postgres_url)    

# Секретный ключ для подписи JWT
SECRET_KEY = 'your_secret_key'


def hash_f(password):
    md5_hash = hashlib.new('md5')
    md5_hash.update(password.encode())
    return md5_hash.hexdigest()

# Функция для создания JWT
def create_token(login):
    payload = {
        'login': login,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Токен действителен 1 час
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Функция для проверки JWT
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['login']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

# Эндпоинт для аутентификации
@app.route('/login', methods=['POST'])
def login():
    login = request.json.get('login')
    password = request.json.get('password')

    Session = sessionmaker(engine)
    with Session() as session:
        user = session.execute(select(Users).where(Users.login == login)).scalar()
        if not user:
            return jsonify({'message': 'User not found'}), 404

        if user.password_hash == hash_f(password):
            token = create_token(login)
            return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

# Защищенный эндпоинт
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 403

    login = verify_token(token)
    if isinstance(login, str) and 'Token' in login:
        return jsonify({'message': login}), 403

    return jsonify({'message': f'Hello, {login}! This is a protected route.'})

# Эндпоинт для создания пользователя
@app.route('/register', methods=['POST'])
def register():
    
    name = request.json.get('name')
    password = request.json.get('password')
    surname = request.json.get('surname')
    patronymic = request.json.get('patronymic')
    login = request.json.get('login')
    
    if not login or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    Session = sessionmaker(engine)
    with Session() as session:
        existing_user = session.execute(select(Users).where(Users.login == login)).scalar()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 409

        new_user = Users(
            name=name,
            login=login, 
            surname=surname,
            patronymic=patronymic,
            password_hash=hash_f(password))
        session.add(new_user)
        session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/search', methods=['GET'])
def search():

    return jsonify({'message': 'User deleted successfully'}), 200