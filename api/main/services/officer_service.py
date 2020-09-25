import jwt
import json
import uuid
import datetime
from flask_api import status
from flask_httpauth import HTTPTokenAuth
from sqlalchemy import exc as sa_exc
from api.main.db import Session
from api.main.config import BCRYPT, SECRET_KEY
from api.main.models.officer_model import Officer


class OfficerService:

    @staticmethod
    def register_officer(username, email, password):
        session = Session()
        try:
            officer = session.query(Officer).filter_by(username=username).first()
            if not officer:
                new_officer = Officer(
                    username=username,
                    email=email,
                    password_hash=BCRYPT.generate_password_hash(password).decode('utf-8')
                )
                session.add(new_officer)
                session.commit()
                auth_token_response = RestaurantAuthService.encode_auth_token(new_restaurant.id)
                if auth_token_response.get('status') == 'success':
                    auth_token = auth_token_response.get('data')
                    return json.dumps({
                        'status': 'success',
                        'message': 'Successfully registered.',
                        'data': new_restaurant.to_dict(),
                        'token': auth_token
                    }), status.HTTP_201_CREATED
                else:
                    return json.dumps(auth_token_response), status.HTTP_400_BAD_REQUEST
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Restaurant already exists. Please Log in.',
                }), status.HTTP_202_ACCEPTED
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def login_restaurant(email, password):
        session = Session()
        try:
            restaurant = session.query(Restaurant).filter_by(email=email).first()
            if restaurant:
                if BCRYPT.check_password_hash(restaurant.password_hash, password):
                    auth_token_response = RestaurantAuthService.encode_auth_token(restaurant.id)
                    if auth_token_response.get('status') == 'success':
                        auth_token = auth_token_response.get('data')
                        return json.dumps({
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'data': restaurant.to_dict(),
                            'token': auth_token
                        }), status.HTTP_200_OK
                    else:
                        return json.dumps(auth_token_response), status.HTTP_400_BAD_REQUEST
                else:
                    return json.dumps({
                        'status': 'fail',
                        'message': 'Password does not match.'
                    }), status.HTTP_400_BAD_REQUEST
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Restaurant does not exist.'
                }), status.HTTP_400_BAD_REQUEST
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def logout_restaurant(auth_token):
        session = Session()
        try:
            blacklist_token = RestaurantBlacklistToken(auth_token)
            session.add(blacklist_token)
            session.commit()
            return json.dumps({
                "status": "success",
                "message": "Successfully logged out."
            }), status.HTTP_200_OK
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def get_restaurant(restaurant_id):
        session = Session()
        try:
            restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
            if restaurant:
                return json.dumps({
                    'status': 'success',
                    'message': 'Get restaurant information.',
                    'data': restaurant.to_dict()
                }), status.HTTP_200_OK
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Restaurant not found.',
                }), status.HTTP_400_BAD_REQUEST
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def get_all_restaurant():
        session = Session()
        try:
            restaurants = session.query(Restaurant).all()
            return json.dumps({
                'status': 'success',
                'message': 'Get all restaurants information.',
                'data': [restaurant.to_dict() for restaurant in restaurants]
            }), status.HTTP_200_OK
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def update(restaurant_id, email=None, password=None, name=None, description=None,
               street_address=None, unit_number=None, country=None, postal_code=None):
        session = Session()
        try:
            record = session.query(Restaurant).filter_by(id=restaurant_id)
            if record.count():
                updates = {}
                if email is not None:
                    updates['email'] = email
                if password is not None:
                    updates['password_hash'] = BCRYPT.generate_password_hash(password).decode('utf-8')
                if name is not None:
                    updates['name'] = name
                if description is not None:
                    updates['description'] = description
                if street_address is not None:
                    updates['street_address'] = street_address
                if unit_number is not None:
                    updates['unit_number'] = unit_number
                if country is not None:
                    updates['country'] = country
                if postal_code is not None:
                    updates['postal_code'] = postal_code
                record.update(updates, synchronize_session='fetch')
                session.commit()
                restaurant = record.first()
                return json.dumps({
                    'status': 'success',
                    'message': 'Restaurant updated.',
                    'data': restaurant.to_dict()
                }), status.HTTP_200_OK
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Restaurant not found.',
                }), status.HTTP_400_BAD_REQUEST
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def delete(restaurant_id):
        session = Session()
        try:
            record = session.query(Restaurant).filter_by(id=restaurant_id).delete()
            if record:
                session.commit()
                return json.dumps({
                    'status': 'success',
                    'message': 'Restaurant deleted.',
                }), status.HTTP_200_OK
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Restaurant not found.',
                }), status.HTTP_400_BAD_REQUEST
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()

    @staticmethod
    def refresh_restaurant_auth_token(restaurant_id):
        auth_token_response = RestaurantAuthService.encode_auth_token(restaurant_id)
        if auth_token_response.get('status') == 'success':
            auth_token = auth_token_response.get('data')
            return json.dumps({
                'status': 'success',
                'message': 'Successfully refreshed token.',
                'restaurant_id': restaurant_id,
                'token': auth_token
            }), status.HTTP_200_OK
        else:
            return json.dumps(auth_token_response), status.HTTP_400_BAD_REQUEST


RESTAURANT_TOKEN_AUTH = HTTPTokenAuth()


@RESTAURANT_TOKEN_AUTH.verify_token
def verify_token(auth_token):
    response = RestaurantAuthService.decode_auth_token(auth_token)
    token_data = response.get('data')
    if response.get('status') == 'success' and token_data.get('role') == 'restaurant':
        return token_data.get('sub')


class RestaurantAuthService:
    @staticmethod
    def encode_auth_token(restaurant_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=4),
                'iat': datetime.datetime.utcnow(),
                'sub': restaurant_id,
                'role': 'restaurant'
            }
            token = jwt.encode(
                key=SECRET_KEY,
                payload=payload,
                algorithm='HS256'
            ).decode()
            return {
                'status': 'success',
                'message': 'Token encoded.',
                'data': token
            }
        except Exception as e:
            return {
                'status': 'fail',
                'message': e,
            }

    @staticmethod
    def decode_auth_token(auth_token):
        is_blacklisted_token = RestaurantAuthService.check_blacklist(auth_token)
        if not is_blacklisted_token:
            try:
                payload = jwt.decode(auth_token, SECRET_KEY)
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
        else:
            return {
                'status': 'fail',
                'message': 'Token blacklisted. Please log in again.'
            }

    @staticmethod
    def check_blacklist(auth_token):
        session = Session()
        result = session.query(RestaurantBlacklistToken).filter_by(token=str(auth_token)).first() is not None
        session.close()
        return result
