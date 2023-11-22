#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ It returns the list of City instances with state_id equals to
                the current State.id => It is the FileStorage relationship
                between State and City """
            city_list = [city for city in list(models.storage.all(City)
                         .values()) if city.state_id == self.id]
            return city_list
