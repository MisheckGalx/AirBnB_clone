#!/usr/bin/python3
'''Class for Place Model'''
from .base_model import BaseModel

class Place(BaseModel):
    '''Place Model'''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    def __init__(self, *args, **kwargs):
        if kwargs.get("user") and kwargs.get("user_id"):
            kwargs.get("user").id = kwargs.get("user_id")
        
        if kwargs.get("city") and kwargs.get("city_id"):
            kwargs.get("city").id = kwargs.get("city_id")

        super().__init__(*args, **kwargs)