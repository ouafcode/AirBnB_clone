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
        """updates the public instance attribute updated_at \
        with the current datetime"""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
          
         
    def __str__(self):
        "print: [<class name>] (<self.id>) <self.__dict__>"
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
   
    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values \
        of __dict__ of the instance"""

        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = \
            datetime.isoformat(dictionary.get('created_at'))
        dictionary['updated_at'] = \
            datetime.isoformat(dictionary.get('updated_at'))
        return dictionary