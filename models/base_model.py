#!/usr/bin/python3
"""Base model"""
import uuid 
from datetime import datetime
from models import storage


class BaseModel:
    """define  class BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialization of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
    def save(self):
        """Save the instance to the storage."""
        # Update the updated_at attribute
        self.updated_at = datetime.now()
        # Save the instance to the storage
        storage.save()              
         
    def __str__(self):
        "print: [<class name>] (<self.id>) <self.__dict__>"
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
   
    def to_dict(self):
        "returns a dictionary containing all keys/values of __dict__"
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict