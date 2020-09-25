from api.main.config import config_by_name
from flask import Blueprint
from flask_restplus import Api
from api.main.controllers.user_controller import API as USER_NS
from api.main.controllers.restaurant_controller import API as RESTAURANT_NS

NAMESPACES = [
    USER_NS,
    RESTAURANT_NS,
]


def create_blueprint():
    bp = Blueprint(
        'main',
        __name__,
        url_prefix='/api/v1'
    )
    api = Api(
        app=bp, version="1.0",
        title="BZZ API",
        description="BZZ API Developer Guide"
    )
    for ns in NAMESPACES:
        api.add_namespace(ns)
    return bp


MAIN_BP = create_blueprint()
