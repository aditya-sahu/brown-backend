def serialize_party(party):
    party["_id"] = str(party["_id"])  # Convert ObjectId to string
    return party
