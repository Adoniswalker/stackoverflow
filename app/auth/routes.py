from flask import request, jsonify

from app import app

users = []
@app.route("/users/signup/", methods=['POST'])
def signup():
    user = request.get_json()
    users.append(user)
    return jsonify(user)


@app.route("/users/all/", methods=['GET'])
def get_users():
    return jsonify(users)