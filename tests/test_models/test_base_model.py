#!/usr/bin/python3
'''Unittests for BaseModel'''
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    #task 3 and below
    def test_id_is_string(self):
        """Tests whether BaseModel.id is a string"""
        self.assertIsInstance(BaseModel().id, str)

    def test_to_dict(self):
        '''Test whether the returned data from method BaseModel.to_dict is a dictionary'''
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_to_dict_created_at(self):
        '''Tests whether value for created_at in returned data from BaseModel.to_dict is a string'''
        self.assertIsInstance(BaseModel().to_dict().get("created_at"), str)

    def test_to_dict_updated_at(self):
        '''Tests whether value for updated_at in returned data from BaseModel.to_dict is a string'''
        self.assertIsInstance(BaseModel().to_dict().get("updated_at"), str)

    #task 4 and above
    def test_new_model_from_dict(self):
        '''Tests whether the new created model from dict has the correct data from to_dict method'''
        d = BaseModel().to_dict()
        self.assertTrue(d == BaseModel(**d))
