#!/usr/bin/python3
"""Class city that imports the BaseModel class for inheritance """
from models.base_model import BaseModel


class City(BaseModel):
    """Class variable to store the state ID associated with the city """
    state_id = ""
    """ Class variable to  store the name of the city """
    name = ""
