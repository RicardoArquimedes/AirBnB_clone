#!/usr/bin/python3
"""
Console
"""
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage


classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):

    """command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ This command send quit signal"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves to JSON file"""
        if arg in classes:
            new_object = classes[arg]()
            new_object.save()
            print(new_object.id)
        elif len(arg) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
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
            storage.reload()
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0] and\
                        instance.id == args[1]:
                    del(instance)
                    del(storage.all()[key])
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        args = split(arg)
        if args == []:
            pass
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            storage.reload()
            new_list = []
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0]:
                    new_list.append(instance.__str__())
            print(new_list)

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
        else:
            storage.reload()
            for key, instance in new_list.items():
                if instance.__class__.__name__ == args[0] and\
                     instance.id == args[1]:
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(args) == 3:
                        print("** value missing **")
                        return
                    else:
                        k_obj = args[0] + "." + args[1]
                        print(k_obj)
                        object = new_list[k_obj]
                        print("-> {}".format(new_list[k_obj]))
                        setattr(object, args[2], args[3])
                        object.save()
                        return
            print("** no instance found **")

if __name__ == "__main__":
    """ Main method """
    HBNBCommand().cmdloop()
