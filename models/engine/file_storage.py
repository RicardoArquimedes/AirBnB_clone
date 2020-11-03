#!/usr/bin/python3
"""
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instance
"""

import json


class FileStorage:

    """
    class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        init
        """
        pass

    def all(self):
        """
        Return dictionary objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj : obj.id
        """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Save - serializate
        """
        json_file = {}
        with open(FileStorage.__file_path, 'w') as jd:
            for key, value in self.__objects.items():
                json_file[key] = value.to_dict()
            json.dump(json_file, jd)

    def reload(self):
        """
        reload - deseralize JSON
        """
        try:
            with open(FileStorage.__file_path, 'r') as jsonf:
                jdict = json.load(jsonf)
            for key, value in jdict.items():
                clss = key.split(".")
                FileStorage.__objets[key] = globals()[clss[0]](**value)
        except:
            pass
