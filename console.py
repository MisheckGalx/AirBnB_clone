#!/usr/bin/python3
'''Entry point to command interpreter'''
import cmd
from models import get_all_model_classes, storage


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for Models"""
    intro = ""
    prompt = "(hbnb) "
    def default(self, line):
    	'''Overridden method'''
    	# try to check if cmd entered is in form <class name>.<method>()
    	cmd_all = line.split('.all()')
    	cmd_count = line.split('.count()')
    	cmd_show = line.split('.show')
    	cmd_destroy = line.split('.destroy')
    	cmd_update = line.split('.update')
    	
    	def unbracketify(s:str):
    		'''Removes brackets and returns string inside the brackets'''
    		s = s.replace('(', '').replace(')', '')
    		if not s.startswith('"') or not s.endswith('"'):
    			return "error-id-given-as-argument"
    		return s.replace('"', '').replace("'", '')
    	
    	if len(cmd_all) == 2:
    		#form = <class name>.all()
    		#cmd = all <class name>
    		args = cmd_all[0]
    		return self.do_all(args)
    		
    	if len(cmd_count) == 2:
    		#form = <class name>.count()
    		#cmd = count <class name>, but not implemented yet but the method
    		# is set to _do_count instead of do_count for the command "count" not to be recognised
    		args = cmd_count[0]
    		return self._do_count(args)
    		
    	if len(cmd_show) == 2 and cmd_show[-1].startswith('(') and cmd_show[-1].endswith(')'):
    		#form = <class name>.show("<id>")
    		#cmd = show <class name> <id>
    		args = cmd_show[0] + " " + unbracketify(cmd_show[-1])
    		return self.do_show(args)
    		
    	if len(cmd_destroy) == 2 and cmd_destroy[-1].startswith('(') and cmd_destroy[-1].endswith(')'):
    		#form = <class name>.destroy("<id>")
    		#cmd = destroy <class name> <id>
    		args = cmd_destroy[0] + " " + unbracketify(cmd_destroy[-1])
    		return self.do_destroy(args)
    		
    	if len(cmd_update) == 2 and cmd_update[-1].startswith('(') and cmd_update[-1].endswith(')'):
    		#form = <class name>.update("<id>", "<attrib>", "<value>") or
    		# <class name>.update("<id>", <dictionary representation>) 
    		#cmd = update <class name> <id> <attrib> <value>
    		try:
    			code = 'setattr(self, "temp_args",list(%s))'%cmd_update[-1]
    			exec(code)    			

    			if len(self.temp_args) > 2:
    				#no dict repr as argument
    				args = '%s %s %s %s'%(cmd_update[0], self.temp_args[0], self.temp_args[1], self.temp_args[2])
    				return self.do_update(args)
    			
    			if len(self.temp_args) == 2:
    				#there is dict repr as argument
    				for key in self.temp_args[-1]:
    					val = self.temp_args[-1].get(key)
    					args = '%s %s %s %s'%(cmd_update[0], self.temp_args[0], key, val)
    					self.do_update(args)
    				return    			
    		except Exception as e:
    			pass
    		
    	return super().default(line)    	

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def emptyline(self) -> bool:
        '''Empty line method called on empty line'''
        return

    def do_EOF(self, arg):
        '''Quit command to exit the program'''
        return self.do_quit(arg)

    def do_help(self, arg: str):
        '''Show documentation on specific command'''
        return super().do_help(arg)
    
    # from Console 0.1
    def do_create(self, classname):
        '''Creates new BaseModel instance'''
        if not classname:
            print("** class name missing **")
        else:
            try:
                model_classes = get_all_model_classes()
                model_class = None
                for model_klass in model_classes:
                    if model_klass.to_classname() == classname:
                        model_class = model_klass
                if not model_class:
                    raise ImportError(" class doesn't exist")
                # class does exist, create new model
                new_model = model_class()
                new_model.save()
                print(new_model.id)
            except ImportError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Shows a string representation of an instance based on classname and id"""
        classname = None
        id = None
        args = line.split(" ")

        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            id = args[1]

        if not classname:
            print("** class name missing **")
        else:
            try:
                model_classes = get_all_model_classes()
                model_class = None
                for model_klass in model_classes:
                    if model_klass.to_classname() == classname:
                        model_class = model_klass
                if not model_class:
                    raise ImportError(" class doesn't exist")
                # class does exist
                if not id:
                    print("** instance id missing **")
                else:
                    #everything is provided
                    obj = None
                    all = storage.all()
                    for key in all:
                        if key == f"{classname}.{id}":
                            obj = all.get(key)
                    if not obj:
                        print("** no instance found **")
                    else:
                        #object found, show it
                        print(str(obj))
            except ImportError:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on classname and id"""
        classname = None
        id = None
        args = line.split(" ")

        if len(args) > 0:
            classname = args[0]

        if len(args) > 1:
            id = args[1]

        if not classname:
            print("** class name missing **")
        else:
            try:
                model_classes = get_all_model_classes()
                model_class = None
                for model_klass in model_classes:
                    if model_klass.to_classname() == classname:
                        model_class = model_klass
                if not model_class:
                    raise ImportError(" class doesn't exist")
                # class does exist
                if not id:
                    print("** instance id missing **")
                else:
                    #everything is provided
                    obj = None
                    all = storage.all()
                    for key in all:
                        if key == f"{classname}.{id}":
                            obj = all.get(key)
                    if not obj:
                        print("** no instance found **")
                    else:
                        #instance found, destroy it
                        storage.all().pop(f"{classname}.{id}")
                        storage.save()
            except ImportError:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on classname"""
        classname = None
        args = line.split(" ")

        if len(args) > 0:
            classname = args[0]
            
        if classname:
            try:
                model_classes = get_all_model_classes()
                model_class = None
                for model_klass in model_classes:
                    if model_klass.to_classname() == classname:
                        model_class = model_klass
                if not model_class:
                    raise ImportError(" class doesn't exist")
                # class does exist
                print([str(storage.all().get(md)) for md in storage.all() if md.startswith(classname)])

            except ImportError:
                print("** class doesn't exist **")

        else:
            print([str(storage.all().get(md)) for md in storage.all()])
            
    def _do_count(self, line):
    	"""Prints number of model instances based on classname"""
    	classname = None
    	args = line.split(" ")    	

    	if len(args) > 0:
    		classname = args[0]
    	
    	if classname:
    		try:
    			model_classes = get_all_model_classes()
    			model_class = None
    			for model_klass in model_classes:
    				if model_klass.to_classname() == classname:
    					model_class = model_klass
    			if not model_class:
    				raise ImportError(" class doesn't exist")
    			# class does exist
    			print(len([str(storage.all().get(md)) for md in storage.all() if md.startswith(classname)]))
    			
    		except ImportError:
    			print("** class doesn't exist **")
    	else:
    		print("** class name missing **")

    def do_update(self, line):
        """Updates an instance based on classname and id by adding or updating an attribute"""
        classname = None
        id = None
        attrib = None
        value = None
        args = line.split(" ")

        if len(args) > 0:
            classname = args[0]
            
        if len(args) > 1:
            id = args[1]

        if len(args) > 2:
            attrib = args[2]

        if len(args) > 3:
            value = args[3]

        if not classname:
            print("** class name missing **")
            
        else:
            try:
                model_classes = get_all_model_classes()
                model_class = None
                for model_klass in model_classes:
                    if model_klass.to_classname() == classname:
                        model_class = model_klass
                if not model_class:
                    raise ImportError(" class doesn't exist")
                    
                # class does exist
                if not id:
                    print("** instance id missing **")
                else:
                    #everything is provided
                    obj = None
                    all = storage.all()
                    for key in all:
                        if key == f"{classname}.{id}":
                            obj = all.get(key)

                    if not obj:
                        print("** no instance found **")
                    else:
                        #instance found, update/set an attribute
                        if attrib and value is not None:
                            if not attrib in ["id", "created_at", "updated_at"]:
                                value = value.replace('"', '')
                                obj.__setattr__(attrib, value)
                                #updating object and saving it
                                obj.save()
                        else:
                            if not attrib:
                                print("** attribute name missing **")
                            elif not value:
                                print("** value missing **")

            except ImportError:
                print("** class doesn't exist **")    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
