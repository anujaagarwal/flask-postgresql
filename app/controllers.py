import datetime
from app import app, db
from flask import jsonify, request
from models import User, Event, Ticket

# Signup endpoint
@app.route('/signup', methods=['POST'])
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
def protected():
    # Perform actions for authenticated user
    return jsonify({'message': 'Protected endpoint accessed successfully.'}), 200
