#!/usr/bin/python3
"""
Console
"""

import cmd


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

if __name__ == "__main__":
    """ Main method """
    HBNBCommand().cmdloop()
