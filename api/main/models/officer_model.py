import re
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import validates, relationship
from api.main.models import Base


EMAIL_REGEX = re.compile(r'\S+@\S+\.\S+')


class Officer(Base):
    __tablename__ = 'officer'
    username = Column(String(255), primary_key=True, unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    @validates('email')
    def validate_email(self, key, address):
        assert EMAIL_REGEX.match(address)
        return address

    def to_dict(self):
        result = {
            'username': self.username,
            'email': self.email,
        }
        return result
