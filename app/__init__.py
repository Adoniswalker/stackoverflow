"""This file is used to initialise this package and create app,also running the server"""
import logging

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app, ) # todo ensure that cors only accepts requests from frontend set env variables
logging.getLogger('flask_cors').level = logging.DEBUG
app.config['CORS_HEADERS'] = 'Content-Type'
from app.auth import routes

app.config.from_object('config.DevelopmentConfig')