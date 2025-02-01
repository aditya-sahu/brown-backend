
from flask import Blueprint, jsonify, abort
from bson import ObjectId
from db import db
from seralize import serialize_party

join_party_api = Blueprint('join_party_api', __name__)



@join_party_api.route('/party/<party_code>', methods=['GET'])
def join_party(party_code):
    party_collection = db["party_collection"]
    party=party_collection.find_one({"party.party_code": party_code})

    if not party:
        return jsonify({"error": "Party Not Found"}), 404

        
        
    return jsonify({
        "party_details": serialize_party(party)
    })

   

@join_party_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error.description)}), 404


