from flask import Blueprint, request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from .models import User, UserSchema, db
import datetime

module = Blueprint('auth', __name__, url_prefix='/auth')
user_schema = UserSchema()

@module.route('/user/', methods=['post'])
def postUser():
    data = request.get_json()
    name = data['name']
    password = data['password']
    if User.query.filter_by(name=name).first():
        return {'result' : 'User {} already exist'.format(name)}
    newUser = User(name=name, password=password)
    db.session.add(newUser)
    db.session.commit()
    return {'result' : 'Add new user with name={}'.format(name)}

@module.route('/login/', methods=['post'])
def loginUser():
    data = request.get_json()
    name = data['name']
    current_user = User.query.filter_by(name=name).first()
    if not current_user:
        return {'result' : 'User {} not fount'.format(name)}
    
    expires = datetime.timedelta(minutes=10)
    access_token = create_access_token(identity = name, expires_delta=expires)
    refresh_token = create_refresh_token(identity = name)
    return {
            'message': 'Logged in as {}'.format(name),
            'access_token': access_token,
            'refresh_token': refresh_token
            }

@module.route('/user/', methods=['get'])
@jwt_required
def getInfo():
    return {
        'result' : 20
    }