from flask import Blueprint, jsonify, request, abort
from db import db
from bson import ObjectId
from pydantic import BaseModel, EmailStr
from seralize import serialize_party

class Login(BaseModel):
    email: EmailStr
    username: str

login_api = Blueprint('login_api', __name__) 

@login_api.route('/login', methods=['POST'])
def login():
    print("In login api")
    login_details = Login.parse_raw(request.data)
    party_collection = db["party_collection"]
    user=party_collection.find_one({"host.username": login_details.username, "host.email": login_details.email})
    print(user)
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    return jsonify({
        "user_details": serialize_party(user),
    })
    return jsonify({'consent': True})
