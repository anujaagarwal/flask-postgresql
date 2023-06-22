from flask_cors import cross_origin
from app.app import app
from flask import jsonify, request
from app.database import conn
from passlib.hash import bcrypt
import jwt


# Signup endpoint
@app.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    data = request.get_json()
    nickname = data['nickname']
    password = data['password']

    # Check if nickname is already taken
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT COUNT(*) FROM users WHERE nickname = %s;",
            (nickname,)
        )
        count = cursor.fetchone()[0]
    if count > 0:
        return jsonify({'message': 'Nickname is already taken.'}), 400

    # Hash the password
    hashed_password = bcrypt.hash(password)

    # Store the user in the database
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (nickname, password) VALUES (%s, %s);",
            (nickname, hashed_password)
        )
        conn.commit()

    return jsonify({'message': 'Signup successful.'}), 201

# Login endpoint
@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    nickname = data['nickname']
    password = data['password']

    # Retrieve user from the database
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT password FROM users WHERE nickname = %s;",
            (nickname,)
        )
        result = cursor.fetchone()
    if result is None:
        return jsonify({'message': 'Invalid nickname or password.'}), 401

    hashed_password = result[0]

    # Verify the password
    if not bcrypt.verify(password, hashed_password):
        return jsonify({'message': 'Invalid nickname or password.'}), 401

    return jsonify({'message': 'Login successful.'}), 200

# Protected endpoint
@app.route('/protected')
@cross_origin()
def protected():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'No token provided.'}), 401

    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'])
        nickname = decoded_token['nickname']
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token.'}), 403

    # Perform actions for authenticated user
    return jsonify({'message': f'Hello, {nickname}! Protected endpoint accessed successfully.'}), 200
