#!/usr/bin/python3

"""The HBnB console"""

import cmd
import sys

from sys.user import User
from sys.datetime import Datetime
from sys.place import Place
from sys.city import City
from sys.state import State
from sys.amenity import Amenity
from sys.review import Review
from shlex import shlex

class HBNBCommand(cmd.Cmd):
	prompt = '(hbnb)'
	clslist = {'Basemodel': Basemodel, 'User': User,'Datetime':Datetime,'Place': Place, 'City': City, 'State': State, 'Amenity': Amenity, 'Review': Review}

	def emptyline(self):
		pass

	def do_create(self,clsname=None):
		if not clsname or clsnamenot in self.clslist:
			print('** class name missing **')
		else:
			obj = self.clslist[clsname]()
			models.storage.save()
			print(obj.id)

	def do_show(self,arg):
		clsname, objid = arg.split(' ')
		key = f"{clsname}.{objid}"
		if key in models.storage.all():
			del models.storage.all()[key]
			models.storage.save()
		else:
			print('** no instance found **')

	def do_all(self,arg):
		objs = [str(v) for v in models.storage.all().values()] if not arg else \
               [str(v) for v in models.storage.all().values() if type(v).__name__ == arg]
	print(objs)
	def do_update(self, arg):
		args = arg.split(' ',3)
		if len(args) == 4:
			clsname, objid, attrname, attrval = args
		obj = models.storage.all().get(f"{clsname}.{objid}", None)
		if obj:
				setattr(obj, attrname, eval(attrval))
				obj.updated_at = datetime.now()
				models.storage.save()
		else:
				print('** no instance found **')

	def do_quit(self, arg):
		return True

	def do_EOF(self, arg):
		return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
