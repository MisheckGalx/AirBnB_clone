#!/usr/bin/python3
'''Class for Review Model'''
from .base_model import BaseModel

class Review(BaseModel):
    '''Review Model'''
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        if kwargs.get("place") and kwargs.get("place_id"):
            kwargs.get("place").id = kwargs.get("place_id")
        
        if kwargs.get("user") and kwargs.get("user_id"):
            kwargs.get("user").id = kwargs.get("user_id")

        super().__init__(*args, **kwargs)