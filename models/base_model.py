#!/usr/bin/python3
""" class Base Model defines that attributes/methods for other classes """
import uuid
from datetime import datetime
import models


def imp_fct():
    # Importing locally to avoid circular import
    from models import storage


class BaseModel():
    """ Define BaseModel class """
    def __init__(self, *args, **kwargs):
        """ Initialisation of Instance

        Args:
            - *args: list of args
            - **kwargs: key and value args in dict format
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ return string representation """
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """ update the date with the current date """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dict with all keys/values """
        dict_1 = self.__dict__.copy()
        dict_1["__clas__"] = type(self).__name__
        dict_1["created_at"] = dict_1["created_at"].isoformat()
        dict_1["updated_at"] = dict_1["updated_at"].isoformat()

        return (dict_1)
