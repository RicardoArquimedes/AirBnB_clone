#!/usr/bin/python3
"""
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instance
"""

import json
from models.base_model import BaseModel
from models.user import User 
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Save - serializate
        """
        json_file = {}
        for key, value in self.__objects.items():
            json_file[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as jfile:
            json.dump(json_file, jfile)

    def reload(self):
        """
        reload - deseralize JSON
        """
        try:
            with open(self.__file_path, 'r') as jsonf:
                jdict = json.load(jsonf)
            for key, value in jdict.items():
                value = eval(value["__class__"])(**value)
                self.__objects[key] = value
        except FileNotFoundError:
            pass
