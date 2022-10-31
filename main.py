from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

users = [] # tuple, list, sets
@app.route("/users/signup", methods=['POST'])
def signup():
    user = request.get_json()
    users.append(user)
    return jsonify(user)

@app.route("/users/all/", methods=['GET'])
def get_users():
#     import pdb;pdb.set_trace()
    return jsonify(users)