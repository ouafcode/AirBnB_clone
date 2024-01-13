#!/usr/bin/python3
""" serialization amd deserialization Instances """
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """ Define class filestorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary """
        return (FileStorage.__objects)

    def new(self, obj):
        """ sets in objects new key /value """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict1 = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict1, f)

    def reload(self):
        """  deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                obj_dict = json.load(f)
            for k, v in obj_dict.items():
                cls_name = v.get('__class__')
                obj = cls_name + '(**v)'
                FileStorage.__objects[k] = obj

        except FileNotFoundError:
            pass
