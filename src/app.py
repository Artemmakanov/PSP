from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,  MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column

import jwt
import datetime

from config import conf

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = conf.postgres_url


# Секретный ключ для подписи JWT
SECRET_KEY = 'your_secret_key'

engine = create_engine(conf.postgres_url)

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    login = Column(String)
    password_hash = Column(String)

class Papers(db.Model):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link_ru = Column(String)
    link_en = Column(String)
    filepath = Column(String)

class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    paper_id = mapped_column(Integer, ForeignKey("papers.id"))


def get_users():
    with Session(engine) as session:
        result = session.execute(select(User.name))
    return result.all()




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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)