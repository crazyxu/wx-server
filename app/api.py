# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request, jsonify
from models import DisplayImage
from utils import AlchemyEncoder
import json
from app import Session
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/v1/images.json', methods=['GET'])
def get_images():
    session = Session()
    image_type = request.args.get('type')
    images = session.query(DisplayImage).filter_by(type=image_type).all()
    res = json.dumps(images, cls=AlchemyEncoder, encoding='utf-8')
    session.close()
    return res

@app.route('/api/v1/images.json', methods=['POST'])
def post_images():
    session = Session()
    if 'type' in request.form and 'url' in request.form:
        image_type = request.form['type']
        image_url = request.form['url']
        session.add(DisplayImage(url=image_url, type=image_type))
        session.commit()
        session.close()
        return handle_response({'success': True})
    else:
        return handle_response({'success': False, 'msg': 'invalid post data'})


def handle_response(obj):
    return json.dumps(obj, cls=AlchemyEncoder)
