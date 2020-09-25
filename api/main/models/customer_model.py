from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.main.models import Base


class Customer(Base):
    __tablename__ = 'customer'
    code = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    dob = Column(DateTime, nullable=False)
    branch_code = Column(Integer, nullable=False)
    image_link = Column(String(1048), nullable=False)
    officer_username = Column(Integer, ForeignKey('officer.username'), nullable=False)

    officer = relationship('Officer', back_populates='customers')

    def to_dict(self):
        result = {
            'code': self.code,
            'name': self.name,
            'age': self.age,
            'dob': self.dob,
            'branch_code': self.branch_code,
            'image_link': self.image_link,
            'officer_username': self.officer_username
        }
        return result
