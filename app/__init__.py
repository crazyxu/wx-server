from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS, cross_origin
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__, static_url_path='')
engine = create_engine("mysql://root:1234567890@localhost:3306/tongying?charset=utf8",
                    encoding='utf-8', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
CORS(app, resources={r"/api/*": {"origins": "*"}})
#
# from app import views
from app import api
from app import session
from app import Base
