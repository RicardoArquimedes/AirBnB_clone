#!/usr/bin/python3
"""
Console CDM for AirBnB clone
Module implementation
"""

import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
           'Place': Place, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):

    """ Command interpreter cmd for AirBnB clone
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ This command send quit signal
        """
        return True

    def emptyline(self):
        """ Quits the command prompt
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        and saves to JSON file"""
        args = split(arg)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instance = classes.get(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = split(arg)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0]\
                        and instance.id == args[1]:
                    print(instance.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0] and\
                        instance.id == args[1]:
                    del(storage.all()[key])
                    storage.save()
                    storage.reload()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        new_list = []
        args = split(arg)
        if args == []:
            for key, instance in storage.all().items():
                new_list.append(instance.__str__())
            print(new_list)
        elif args[0] in classes:
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0]:
                    new_list.append(instance.__str__())
            print(new_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Update an instance baed on the class name
        and id by adding or updating attribute
        """
        args = split(arg)
        new_list = storage.all()
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            k_obj = args[0] + "." + args[1]
            if k_obj in new_list:
                object = new_list[k_obj]
                setattr(object, args[2], args[3])
                storage.save()
                storage.reload()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    """ Main method
    """
    HBNBCommand().cmdloop()
