#!/usr/bin/python3
'''Module for all the models'''
import datetime
import uuid
from models import storage

class BaseModel:
    '''BaseModel for All Models'''
    def __init__(self, *args, **kwargs):
        self.updated_at = None
        self.id = None
        self.created_at = None
        self.load_from_dict(kwargs)
        self.prepare()

    @property
    def classname(self):
        '''Returns the object classname'''
        return str(self.__class__).split(".")[-1].split("'")[0].strip()

    @classmethod
    def to_classname(cls):
        '''Returns the object classname'''
        return str(cls).split(".")[-1].split("'")[0].strip()

    def prepare(self):
        '''First method to prepare everything'''
        if not self.id:
            #this was not loaded from json
            #object being created for the first time
            self.set_id()
            self.set_created_at()
            self.set_updated_at()
            storage.new(self)

    def load_from_dict(self, _dict:dict):
        '''Try load an object from dictionary'''
        for key in _dict:
            if key not in ["created_at", "updated_at"]and not key == "__class__":
                setattr(self, key, _dict.get(key))

            elif key == "__class__":
                continue
                
            else:
                #convert string datetime to datetime object
                d = _dict.get(key)
                d = datetime.datetime.fromisoformat(d)
                setattr(self, key, d)

    def set_id(self):
        '''Sets a unique id using uuid4 if not set'''
        if not self.id:
            self.id = str(uuid.uuid4())

    def set_created_at(self):
        '''Sets the datetime this object was created'''
        self.created_at = datetime.datetime.now()

    def set_updated_at(self):
        '''Sets the datetime this object was updated'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''Returns a dict containing all keys/values of __dict__ attrib'''
        d = self.__dict__
        new_dict = {}
        
        for key in d.keys():
            if  (hasattr(d, key) and d.get(key)) != None and key not in [ "created_at", "updated_at"] and len(key.split("__loaded_from_json")) < 2:
                new_dict[f"{key}"] = d.get(key)

            else:
                if key in ["created_at", "updated_at"]:
                    if key == "updated_at":
                        new_dict["__class__"] = self.classname
                    new_dict[f"{key}"] = d.get(key).isoformat()
             
        #adding classname in new_dict
        return new_dict

    def __setattr__(self, __name: str, __value) -> None:
        '''Sets the new attribute'''
        return super().__setattr__(__name, __value)

    def save(self):
        '''Saves this model in a JSON file'''
        self.updated_at = datetime.datetime.now()

        for key in storage.all():
            if key == f"{self.classname}.{self.id}":
                storage.all()[key] = self
        storage.save()

    def __str__(self) -> str:
        '''Str representation'''
        return f"[{self.classname}] ({self.id}){self.__dict__}"
