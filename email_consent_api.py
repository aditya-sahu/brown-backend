from flask import Blueprint, jsonify
from pydantic import BaseModel, EmailStr
class Email_Consent(BaseModel):
    email: EmailStr
    party_code: str

email_consent_api = Blueprint('email_consent_api', __name__) 

@email_consent_api.route('/email_consent', methods=['POST'])
def give_email_consent():
    print("In email consent")
    return jsonify({'consent': True})
