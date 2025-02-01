import hashlib
from pydantic import BaseModel, ValidationError, EmailStr
from flask import Flask, request, jsonify, abort
from db import db
from pymongo import MongoClient


app = Flask(__name__)

from join_party import join_party_api
app.register_blueprint(join_party_api)


from email_consent_api import email_consent_api
app.register_blueprint(email_consent_api)

def generate_party_code(username, email, party_name):
    combined_input = f"{username}{email}{party_name}"
    party_code = hashlib.sha256(combined_input.encode()).hexdigest()[:8]
    return party_code

class Create_Party(BaseModel):
    username: str
    email: EmailStr
    party_name: str

@app.route('/')
def home():
    return jsonify({"status":"Running!"})

@app.route('/generate_party_code', methods=['POST'])
def create_party_code():
    party_collection = db["party_collection"]
    try:
        new_party = Create_Party.parse_raw(request.data)

    
        party_code = generate_party_code(new_party.username, new_party.email, new_party.party_name)

        print(party_code)
        existing_party = party_collection.find_one({"party.party_code": party_code})
        if existing_party:
            return jsonify({"error": "Party code already exists. Try a different party name."}), 400


        party_collection.insert_one({
            "host": {
                "username": new_party.username,
                "email": new_party.email
            },
            "party": {
                "party_code": party_code,
                "party_name": new_party.party_name,
                "user_count": 1
            },
            "users": []
        })
        return jsonify({'party_code': party_code})

    except ValidationError as e:
        return jsonify({'error': str(e)}), 400

class Email_Consent(BaseModel):
    email: EmailStr
    party_code: str


if __name__ == '__main__':
    app.run(debug = True)