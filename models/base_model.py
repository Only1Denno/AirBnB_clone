#!usr/bin/python3
"""Defines class for BaseModel."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Represents base model.
    Represents "base" for AirBnB task classes.
    """

    def __init__(self, *args, **kwargs):
        """Initialize new Base.
        Args:
            *args: Accepts any number of positional arguments.
            **kwargs: Accepts key/pair value arguments.
        """
        """ Define the datetime format for string-to-datetime conversion """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        """  Check if keyword arguments are provided """
        if kwargs:
            """ Iterate through key-value pairs in kwargs """
            for k, v in kwargs.items():
                """ Skip processing "__class__" key """
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    time = datetime.strptime(v, tformat)
                    setattr(self, k, time)
                else:
                    setattr(self, k, v)
                    """ Set other attributes based on key-value pairs """
        else:
            """ If no kwargs provided, initialize with default values """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """  Add the new instance to the storage """
            models.storage.new(self)

    def __str__(self):
        """returs  print/str rep  of BaseModel instance"""
        """ Get the class name and return formatted string """
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

    def save(self):
        """Update the "updated_at" attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all the keys/values"""
        """ Create a copy of the instance dictionary """
        ndict = self.__dict__.copy()
        ndict.update({"created_at": self.created_at.isoformat()})
        ndict.update({"updated_at": self.updated_at.isoformat()})
        """ Add the "__class__" key with the class name """
        ndict.update({"__class__": self.__class__.__name__})
        return (ndict)
