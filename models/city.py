#!/usr/bin/python3
""" classes that inherit from BaseModel """


from models.base_model import BaseModel


class City(BaseModel):
    """ define class city """
    state_id = ""
    name = ""
