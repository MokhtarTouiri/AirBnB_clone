#!/usr/bin/python3
""" MODULE """


import uuid
from datetime import datetime


class BaseModel:
    """ PUBLIC """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ RETURN STRING """
        return "[{}] ({}) {}". \
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ SAVE.SELF """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ SELF """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

