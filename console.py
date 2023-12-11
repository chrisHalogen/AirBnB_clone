#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """This function is responsible for Parsing the
        user input command
    """
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    brackets_match = re.search(r"\[(.*?)\]", arg)
    if curly_braces_match is None:
        if brackets_match is None:
            return [portion.strip(",") for portion in split(arg)]
        else:
            lex = split(arg[:brackets_match.span()[0]])
            output = [portion.strip(",") for portion in lex]
            output.append(brackets_match.group())
            return output
    else:
        lex = split(arg[:curly_braces_match.span()[0]])
        output = [portion.strip(",") for portion in lex]
        output.append(curly_braces_match.group())
        return output


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Pass if line is empty."""
        pass

    def default(self, arg):
        """Default action."""
        arg_method_map_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match_re = re.search(r"\.", arg)
        if match_re is not None:
            argument = [arg[:match_re.span()[0]], arg[match_re.span()[1]:]]
            match_re = re.search(r"\((.*?)\)", argument[1])
            if match_re is not None:
                command = [argument[1][:match_re.span()[0]], match_re.group()[1:-1]]
                if command[0] in arg_method_map_dict.keys():
                    call = "{} {}".format(argument[0], command[1])
                    return arg_method_map_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """CMD to exit program."""
        return True

    def do_EOF(self, arg):
        """EOF to quit program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new instance and show id.
        """
        argument = parse(arg)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argument[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of an id.
        """
        argument = parse(arg)
        object_dict = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(argument[0], argument[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of an id."""
        argument = parse(arg)
        objdict = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argument[0], argument[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a class.
        If no class is given, displays all instantiated objects."""
        argument = parse(arg)
        if len(argument) > 0 and argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for obj in storage.all().values():
                if len(argument) > 0 and argument[0] == obj.__class__.__name__:
                    object_list.append(obj.__str__())
                elif len(argument) == 0:
                    object_list.append(obj.__str__())
            print(object_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Get the number of instances of a class."""
        argument = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argument[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of an id by adding or updating
        an attribute key/value pair or dict."""
        argument = parse(arg)
        object_dict = storage.all()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        if argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argument) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argument[0], argument[1]) not in object_dict.keys():
            print("** no instance found **")
            return False
        if len(argument) == 2:
            print("** attribute name missing **")
            return False
        if len(argument) == 3:
            try:
                type(eval(argument[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argument) == 4:
            obj = object_dict["{}.{}".format(argument[0], argument[1])]
            if argument[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argument[2]])
                obj.__dict__[argument[2]] = valtype(argument[3])
            else:
                obj.__dict__[argument[2]] = argument[3]
        elif type(eval(argument[2])) == dict:
            obj = object_dict["{}.{}".format(argument[0], argument[1])]
            for k, v in eval(argument[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
