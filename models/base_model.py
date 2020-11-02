#!/usr/bin/python3
"""
Base Class
"""
import uuid
from datetime import date, datetime


class BaseModel:

    """
    Base model class that defines all common
    attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        """
        self.update_at = datetime.now()
