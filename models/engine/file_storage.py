#!/usr/bin/python3
'''JSON Serializer'''
import json
from typing import Any


class ModelJSONEncoder(json.JSONEncoder):
    '''JSON Encoder for All Models'''
    def default(self, o: Any) -> Any:
        return o.to_dict()

class FileStorage:
    '''File Storage Class'''
    __file_path = "models.json"
    __objects = {}
    def all(self):
        """Returns all objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in the obj with key <obj class name>.id"""
        key = f"{obj.classname}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        fd = open(self.__file_path, "w")
        s = json.dump(self.__objects, fd, cls=ModelJSONEncoder)
        try:
        	fd.close()
        except:
        	pass

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file [__filepath] exists else pass)"""
        from models import get_all_model_classes
        try:
            d = {}
            objects_dict = json.load(open(self.__file_path, "r"))            

            def get_model_class(classname):
                model_classes = get_all_model_classes()
                model_class = None
                for model_klass in model_classes:
                    if model_klass.to_classname() == classname:
                        model_class = model_klass
                return model_class
                
            for key in objects_dict:
                d[key] = get_model_class(key.split(".")[0])(**objects_dict.get(key))
                
            self.__objects = d
        except:
            pass
