#!/usr/bin/python3
"class FileStorage"
import json
from os import path

class FileStorage:
    "serializes instances to a JSON file and deserializes JSON file"
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        "returns the dictionary __objects"
        return self.__objects
    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"
        serializ_obj = {}
        for key, value in self.__objects.items():
            serializ_obj[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serializ_obj, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    # Import the class dynamically based on class_name
                    cls = globals()[class_name]
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj

storage = FileStorage()
storage.reload()