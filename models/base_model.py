#!/usr/bin/python3
"""In this module BaseModel class is created"""


from datetime import datetime
import uuid
import models


class BaseModel:

    """
    Base model class that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        constructor init
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif not key == "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String of
        an object"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

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
        dict_2 = self.__dict__.copy()
        dict_2['__class__'] = self.__class__.__name__
        dict_2['created_at'] = self.created_at.isoformat()
        dict_2['updated_at'] = self.updated_at.isoformat()
        return dict_2
