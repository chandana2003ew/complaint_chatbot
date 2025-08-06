from flask import Blueprint, request, jsonify
from utils.database import get_db
from utils.auth_utils import encode_token
import hashlib

auth_api = Blueprint('auth', __name__)

@auth_api.route("/register", methods=["POST"])
def register():
    data = request.json
    db = get_db()
    hashed_pw = hashlib.sha256(data['password'].encode()).hexdigest()
    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
               (data['name'], data['email'], hashed_pw))
    db.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_api.route("/login", methods=["POST"])
def login():
    data = request.json
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email = ?", (data['email'],)).fetchone()
    if user and hashlib.sha256(data['password'].encode()).hexdigest() == user['password']:
        token = encode_token(user['id'])
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
