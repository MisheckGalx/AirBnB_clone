#!/usr/bin/python3
'''Class for User Model'''
from .base_model import BaseModel


class User(BaseModel):
    '''User Model'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
