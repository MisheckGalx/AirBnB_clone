#!/usr/bin/python3
'''Class for State Model'''
from .base_model import BaseModel


class State(BaseModel):
    '''State Model'''
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        if kwargs.get("state_id"):
            self.id = kwargs.get("state")
        super().__init__(*args, **kwargs)
