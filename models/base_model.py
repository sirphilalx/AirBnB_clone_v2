#!/usr/bin/python3
"""A BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """ A class that defines all common attributes/methods
        for other classes:"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel class """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, tform)
                if k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """ Updates the public instance attribute updated_at
            with the current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
            of __dict__ of the instance: """
        rdict = dict(self.__dict__)
        rdict["__class__"] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        del rdict["_sa_instance_state"]
        return rdict

    def delete(self):
        """ Deletes the current instance from the storage """
        models.storage.delete(self)

    def __repr__(self):
        """returns string function"""
        return self.__str__()

    def __str__(self):
        """ Returns the description of the BaseModel class"""
        rdict = dict(self.__dict__)
        del rdict["_sa_instance_state"]
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, rdict)
