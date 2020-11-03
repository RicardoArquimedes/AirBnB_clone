#!/usr/bin/python3
"""
Base Class
"""
import uuid
from datetime import date, datetime
import models


class BaseModel:

    """
    Base model class that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                                                    value,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                                                    value,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                elif key == '__class__':
                    pass
                elif key is not "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.save()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/
        valus of __dict__ of the instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
