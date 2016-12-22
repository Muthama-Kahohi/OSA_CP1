#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    amity (-i | --interactive)
    amity (-h | --help | --version)
    amity create_room <room_type> ...
    amity create_person <fname> <lname> <role> [<accomodation>] 
    amity load_people <file_name>
    amity print_allocations [<file_name>]
    amity print_unallocated [<file_name>]
    amity print_room <room_name>
    amity load_state <database_name>
    amity save_state [<db_name>]
    amity reallocate id room_from room_to
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
  
"""

import sys
import csv
import cmd
import sqlite3
from docopt import docopt, DocoptExit
from colorama import init, Fore
init()
from pyfiglet import Figlet
from termcolor import colored

# import my modules
from app.amity import Amity


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class AmitySpaceAllocation (cmd.Cmd):
    f = Figlet(font='slant')
    dojo = Amity()
    # Makes the interface look better
    print(Fore.GREEN + f.renderText('Amity Space Allocation ')).center(10)
    print(Fore.YELLOW + ('Type help to get a list of commands')).center(70)
    print(Fore.YELLOW + ('Type a command to get the arguments it requires')).center(70)

    prompt = '(amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        try:
            room_type = str(arg['<room_type>'])
            room_list = arg['<room_name>']
            if len(room_list) == 1:
                self.dojo.create_room(
                    {"room_type": room_type, "room_name": str(room_list[0])})
            else:
                self.dojo.create_room(
                    {"room_type": room_type, "room_name": room_list})
        except TypeError:
            print(colored("The Values shoud be strings"))

    @docopt_cmd
    def do_create_person(self, arg):
        """Usage: create_person <fname> <lname> <role> [<accomodation>]  
        """
        try:
            first_name = str(arg['<fname>'])
            last_name = str(arg['<lname>'])
            role = str(arg['<role>'])
            accomodation = arg['<accomodation>']
    
        except TypeError:
            print("You have to pass names")
        if accomodation == None:
            wants_accomodation = 'N'
        else:
            wants_accomodation = accomodation    
        self.dojo.create_person(first_name, last_name, role, wants_accomodation)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>
        """
        file_name = arg['<file_name>']
        file_name = file_name + ".txt"
        self.dojo.load_people(file_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<file_name>]
        """
        file_name = arg['<file_name>']
        if file_name:
            file_name = file_name + ".txt"
            self.dojo.print_allocations(file_name)
        else:
            self.dojo.print_allocations()       


    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<file_name>]
        """
        file_name = arg['<file_name>']
        if file_name:
            file_name = file_name + ".txt"
            self.dojo.print_unallocated(file_name)
        else:
            self.dojo.print_unallocated()       

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>

        """
        room_name = arg['<room_name>']
        self.dojo.print_room(room_name)
    
    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [<database_name>]"""
        db_name = arg['<database_name>']
        self.dojo.save_state(db_name)        

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <database_name> 

        """

        db_name = str(arg['<database_name>'])
        self.dojo.load_state(db_name)


    @docopt_cmd
    def do_reallocate(self, arg):
        """Usage: reallocate <id> <room_from> <room_to> """
        try:
            id = str(arg['<id>'])
            room_to = arg["<room_to>"]
            room_from = arg["<room_from>"]
            self.dojo.reallocate(id, room_from, room_to)
        except TypeError:
            print(colored("Invalid database name"))  

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    AmitySpaceAllocation().cmdloop()

print(opt)
