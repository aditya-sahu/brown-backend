from flask import Blueprint, jsonify

email_consent_api = Blueprint('email_consent_api', __name__) 

@email_consent_api.route('/email_consent', methods=['POST'])
def give_email_consent():
    print("In email consent")
    return jsonify({'consent': True})
