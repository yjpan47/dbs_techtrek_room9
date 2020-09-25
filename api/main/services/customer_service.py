import jwt
import json
import requests
from flask_api import status
from sqlalchemy import exc as sa_exc
from api.main.db import Session
from api.main.config import BCRYPT, SECRET_KEY
from api.main.models import Customer
from api.main.models.officer_model import Officer
from flask_httpauth import HTTPTokenAuth


class CustomerService:

    @staticmethod
    def get_customers(officer_username):
        session = Session()
        try:
            customers = session.query(Customer).filter_by(officer_username=officer_username).all()
            return json.dumps({
                'status': 'success',
                'message': 'Get all customers',
                'data': [customer.to_dict() for customer in customers]
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
    def create_customer(code, name, age, dob, branch_code, officer_username):
        session = Session()
        try:
            customer = session.query(Customer).filter_by(code=code).first()
            if not customer:
                new_customer = Customer(
                    code=code,
                    name=name,
                    age=age,
                    dob=dob,
                    branch_code=branch_code,
                    officer_username=officer_username
                )
                session.add(new_customer)
                session.commit()
                return json.dumps({
                    'status': 'success',
                    'message': 'Successfully created customer.',
                    'data': new_customer.to_dict(),
                }), status.HTTP_201_CREATED
            else:
                return json.dumps({
                    'status': 'fail',
                    'message': 'Customer already exists. Please Log in.',
                    }), status.HTTP_202_ACCEPTED
        except sa_exc.SQLAlchemyError:
            session.rollback()
            return json.dumps({
                'status': 'fail',
                'message': 'Internal Server Error.'
            }), status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            session.close()
