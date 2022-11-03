import logging

from flask import Flask
from flask import request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app, ) # todo ensure that cors only accepts requests from frontend set env variables
app.config['CORS_HEADERS'] = 'Content-Type'
users = []


@app.route("/users/signup/", methods=['POST'])
def signup():
    user = request.get_json()
    users.append(user)
    return jsonify(user)


@app.route("/users/all/", methods=['GET'])
def get_users():
    return jsonify(users)
