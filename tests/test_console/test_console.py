#!/usr/bin/python3
'''Unittests for the Console'''
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    '''Test Cases for console'''
    def assertHasAttr(self, obj, attrname, message=None):
        has_attr_msg = "object {} does'nt have attribute \"{}\" "
        if not hasattr(obj, attrname):
            if message is not None:
                self.fail(message)
            else:
                self.fail(has_attr_msg.format(obj, attrname))
                
    def test_prompt(self):
    	'''Tests if the prompt is "(hbnb)"'''
    	self.assertEqual(HBNBCommand().prompt, '(hbnb) ')
    	
    def test_help_command(self):
    	'''Test if output from running "help" command from command line is same as from executing a function'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#running from cmd line
    		cmd.onecmd("help show")
    		first_output = f.getvalue().split('\n')[0]
    		
    		#running from function
    		cmd.do_help("show")
    		second_output = f.getvalue().split('\n')[1]
    		
    		self.assertEqual(first_output, second_output)
    		
    def test_quit_command(self):
    	'''Test if output from running "quit" quits the cmd program'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#running from cmd line
    		cmd.onecmd("quit")
    		self.assertTrue(cmd.exited)
    		
    def test_EOF_command(self):
    	'''Test if output from running "EOF" quits the cmd program'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#running from cmd line
    		cmd.onecmd("EOF")
    		self.assertTrue(cmd.exited)
    		
    def test_create_command(self):
    	'''Test if output from running "create" command from command line creates new BaseModel instance'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#running from cmd line
    		cmd.onecmd("create BaseModel")
    		model_id = f.getvalue().split('\n')[0]
    		model = storage.all().get(f"BaseModel.{model_id}")
    		if model:
    			#delete the new model, we're done with it
    			storage.all().pop(f"BaseModel.{model_id}")
    			storage.save()
    		self.assertIsNotNone(model)
    		
    def test_show(self):
    	'''Test if output from running "show" command from command line shows same output from function'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#first lets create own model
    		cmd.do_create("BaseModel")
    		first_output = f.getvalue().split('\n')[0]
    		model_id = first_output
    		
    		#running from cmd line
    		cmd.onecmd(f"show BaseModel {model_id}")
    		second_output = f.getvalue().split('\n')[1]
    		
    		#running from function
    		cmd.do_show(f"BaseModel {model_id}")
    		third_output = f.getvalue().split('\n')[2]
    		
    		#deleting created model
    		storage.all().pop(f"BaseModel.{model_id}")
    		storage.save()
    		
    		self.assertEqual(second_output, third_output)
    		
    def test_destroy(self):
    	'''Test if running "destroy" command from command line really deletes a model'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#first lets create own model
    		cmd.do_create("BaseModel")
    		first_output = f.getvalue().split('\n')[0]
    		model_id = first_output
    		
    		#running from cmd line
    		cmd.onecmd(f"destroy BaseModel {model_id}")
    		
    		#trying to fetch the model
    		#should be none
    		model = storage.all().get(f"BaseModel.{model_id}")
    		
    		self.assertIsNone(model)
    		
    def test_update(self):
    	'''Test if running "update" command from command line really updates a model'''
    	with patch('sys.stdout', new=StringIO()) as f:
    		cmd = HBNBCommand()
    		#first lets create own model
    		cmd.do_create("BaseModel")
    		first_output = f.getvalue().split('\n')[0]
    		model_id = first_output
    		
    		#running from cmd line
    		cmd.onecmd(f"update BaseModel {model_id} temp_attribute temp_value")
    		
    		#getting model
    		#should not be None
    		model = storage.all().get(f"BaseModel.{model_id}")
    		
    		self.assertIsNotNone(model)
    		#delete the model
    		storage.all().pop(f"BaseModel.{model_id}")
    		storage.save()
    		
    		self.assertHasAttr(model, "temp_attribute")
    		self.assertEqual(model.temp_attribute, "temp_value")
