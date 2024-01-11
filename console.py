#!/usr/bin/python3
""" program for command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ define command class """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ to quit the command ^D """
        print("")
        return True

    def emptyline(self):
        """ shouldn’t execute anything """
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
