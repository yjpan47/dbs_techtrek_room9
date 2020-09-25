
from api.main.config import config_by_name
from flask import Blueprint
from flask_restplus import Api
from api.main.controllers.customer_controller import API as CUSTOMER_NS
from api.main.controllers.officer_controller import API as OFFICER_NS

NAMESPACES = [
    CUSTOMER_NS,
    OFFICER_NS,
]


def create_blueprint():
    bp = Blueprint(
        'main',
        __name__,
        url_prefix='/api/v1'
    )
    api = Api(
        app=bp, version="1.0",
        title="DBS API",
        description="DBS API Developer Guide"
    )
    for ns in NAMESPACES:
        api.add_namespace(ns)
    return bp


MAIN_BP = create_blueprint()
