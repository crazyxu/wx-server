# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request
from models import DisplayImage
from utils import AlchemyEncoder
import json
from app import session
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/v1/images.json', methods=['GET'])
def get_images():
    image_type = request.args.get('type')
    images = session.query(DisplayImage).filter_by(type=image_type).all()
    res = json.dumps(images, cls=AlchemyEncoder, encoding='utf-8')
    print res
    return res

@app.route('/api/v1/images.json', methods=['POST'])
def post_images():
    image_type = request.args.get('type')
    print 'success'
    return 'success'
