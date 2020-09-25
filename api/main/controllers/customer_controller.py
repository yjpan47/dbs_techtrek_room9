import random
from flask import request
from flask_restplus import Resource, Namespace
from api.main.services.customer_service import CustomerService
from api.main.services.officer_service import TOKEN_AUTH

API = Namespace(
    name='customer',
    description='Operations related to adding, retrieving, deleting, and updating data for the customer entity.'
)


MAX_INT = 1000000000


@API.route('/', strict_slashes=False)
class CustomerController(Resource):
    @TOKEN_AUTH.login_required
    def get(self):
        officer_username = TOKEN_AUTH.current_user()
        return CustomerService.get_customers(officer_username)

    @TOKEN_AUTH.login_required
    def post(self):
        officer_username = TOKEN_AUTH.current_user()
        name = request.json.get('name')
        age = request.json.get('age')
        dob = request.json.get('dob')
        branch_code = request.json.get('branch_code')
        return CustomerService.create_customer(
            code=random.randint(1, MAX_INT),
            name=name,
            age=age,
            dob=dob,
            branch_code=branch_code,
            officer_username=officer_username
        )
