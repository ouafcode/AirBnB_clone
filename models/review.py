#!/usr/bin/python3
"""Classes that inherit from BaseModel """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Define Class Review"""
    place_id = ""
    user_id = ""
    text = ""
