import jwt
import json
import requests
from flask_api import status
from sqlalchemy import exc as sa_exc
from api.main.db import Session
from api.main.config import BCRYPT, SECRET_KEY
from api.main.models.officer_model import Officer
from flask_httpauth import HTTPTokenAuth


class OfficerService:

    @staticmethod
    def login_officer(email, password):
        session = Session()
        try:
            officer = session.query(Officer).filter_by(email=email).first()
            if officer:
                if BCRYPT.check_password_hash(officer.password_hash, password):
                    token = OfficerAuthService.encode_auth_token(email, password)
                    return json.dumps({
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'data': officer.to_dict(),
                        'token': token
                    }), status.HTTP_200_OK
                else:
                    return json.dumps({
                        'status': 'fail',
                        'message': 'Password does not match.'
                    }), status.HTTP_400_BAD_REQUEST
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Officer does not exist.'
                }), status.HTTP_400_BAD_REQUEST
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()


class OfficerAuthService:
    @staticmethod
    def encode_auth_token(email, password):
        try:
            url = 'http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login'
            data = {
                'username': email,
                'password': password
            }
            data = requests.post(url, data=data)
            token = data.content.decode()
            return token
        except Exception as e:
            return {
                'status': 'fail',
                'message': e,
            }

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = {
                'token': auth_token,
                'sub': 'ethanee'
            }
            return {
                'status': 'success',
                'message': 'Token decoded.',
                'data': payload
            }
        except jwt.ExpiredSignatureError:
            return {
                'status': 'fail',
                'message': 'Signature expired.'
            }
        except jwt.InvalidTokenError:
            return {
                'status': 'fail',
                'message': 'Invalid token.'
            }


TOKEN_AUTH = HTTPTokenAuth()


@TOKEN_AUTH.verify_token
def verify_token(auth_token):
    response = OfficerAuthService.decode_auth_token(auth_token)
    token_data = response.get('data')
    if response.get('status') == 'success':
        return token_data.get('sub')