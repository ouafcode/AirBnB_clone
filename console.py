#!/usr/bin/python3
""" program for command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ define command class 
    Attribute:
        prompt (str): command prompt showed 
    """

    prompt = "(hbnb)"
    __classe  = {
        "BaseModel"
    }

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

    def do_create(self, arg):
        """ create new class instance """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        else:
            print(arg[0].id)
            storage.save()

    def do_show(self, arg):
        """ print string representation of instance
            base on class name and id
        """
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        if arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        else:
            obj_dit = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    obj_dict.append(obj.str())
                elif len(arg) == 0:
                    obj_dict.append(obj.__str__())
            print(obj_dit)
            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
