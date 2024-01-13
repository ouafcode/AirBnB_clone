#!/usr/bin/python3
""" program for command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """ define command class

    Attribute:
        prompt (str): command prompt showed
    """

    prompt = "(hbnb)"
    __classe = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
        ]

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
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """ print string representation of instance
            base on class name and id
        """
        arg = arg.split()
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
        arg = arg.split()
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
        arg = arg.split()
        if arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        else:
            obj_dit = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == type(obj).__name__:
                    obj_dit.append(obj.__str__())
                elif len(arg) == 0:
                    obj_dit.append(obj.__str__())
            print(obj_dit)

    def do_update(self, arg):
        """  Updates an instance based on the class name and id """
        obj_dict = storage.all()
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classe:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            key = arg[0] + '.' + arg[1]
            obj = obj_dict.get(key, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, arg[2], arg[3].lstrip('"').rstrip('"'))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
