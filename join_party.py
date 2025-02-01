
from flask import Blueprint, jsonify, abort
from db import db

join_party_api = Blueprint('join_party_api', __name__)


@join_party_api.route('/party/<party_code>', methods=['GET'])
def join_party(party_code):
    party_collection = db["party_collection"]
    party=party_collection.find_one({"party.party_code": party_code})

    if not party:
        abort(404, description="Party Not Found")
        
    return jsonify({
        "party_details": party,
    })

   

@join_party_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error.description)}), 404


