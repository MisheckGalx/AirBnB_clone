#!/usr/bin/python3
'''Class for City Model'''
from .base_model import BaseModel

class City(BaseModel):
    '''City Model'''
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        if kwargs.get("state_id"):
            self.id = kwargs.get("state_id")
        super().__init__(*args, **kwargs)
