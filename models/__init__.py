#!/usr/bin/python3
from .engine.file_storage import FileStorage


class JSONFileStorage(FileStorage):
    '''My JSON File Storage'''

def get_all_model_classes():
    from .base_model import BaseModel
    from .user import User
    from .state import State
    from .city import City
    from .amenity import Amenity
    from .place import Place
    from .review import Review
    return [
        BaseModel,
        User,
        State,
        City,
        Amenity,
        Place,
        Review,
    ]

storage = JSONFileStorage()
storage.reload()
