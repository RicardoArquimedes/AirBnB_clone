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

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Return dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj : obj.id
        """
        if obj:
            self.__objects[
                "{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        jsonfile = {}
        with open(self.__file_path, 'w') as fd:
            for key, value in self.__objects.items():
                jsonfile[key] = value.to_dict()
            json.dump(jsonfile, fd)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'w') as fd:
                jsonfile = json.load(fd)
                for key, value in jsonfile.items():
                    clss = key.split(".")
                    FileStorage.__objects[key] = globals()[clss[0]](**value)
        except:
            pass
