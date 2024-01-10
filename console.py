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
        return True
    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
