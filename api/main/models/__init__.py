from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from api.main.models.customer_model import Customer
from api.main.models.officer_model import Officer

