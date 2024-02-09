#!/usr/bin/python3
'''Unittests for the Console'''
import unittest
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    '''Test Cases for console'''

	def setUp(self):
		self.mock_stdin = create_autospec(sys.stdin)
		self.mock_stdout = create_autospec(sys.stdout)
		self.out = StringIO()
		sys.stdout = self.out
		self.c = self.create()
		models.storage._FileStorage__objects.clear()

	def tearDown(self):
		sys.stdout = sys.__stdout__
		self.remove_file('file.json')
		models.storage._FileStorage__objects.clear()
		self.clearIO()

	def remove_file(self, filename):
		try:
			os.remove(filename)
		except FileNotFoundError:
			pass

	def clearIO(self):
		self.out.seek(0)
		self.out.truncate(0)

	def create(self, server=None):
	"""
	Create an instance of the console.

	Parameters:
	- server: Optional parameter representing a server.

	Returns:
	An instance of the HBNBCommand class with mocked standard input and output.
	"""
	return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

	def get_last_write_output(self, num_lines=None):
		if num_line is None:
			return self.mock_stdout.write.call_args[0][0]
		last_outputs = self.mock_stdout.write.call_args_list[-num_lines:]
		concatenated_output = "".join(map(lambda call_args: call_args[0][0], last_outputs))
		return concatenated_output
