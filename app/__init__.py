from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.cors import CORS

app = Flask(__name__, static_url_path='')
# app.config.from_object('config')
# db = SQLAlchemy(app)
# CORS(app)
#
# from app import views
from app import api