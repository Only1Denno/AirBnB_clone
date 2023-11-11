#!/usr/bin/python3
"""Class Amenity which imports the BaseModel class from models.base_model"""
from models.base_model import BaseModel

""" Defines a new class Amenity that inherits from BaseModel """
class Amenity(BaseModel):
    """ initialize a class attribute 'name' with empty string"""
    name = ""
