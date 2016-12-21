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

# import my modules


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

    # Makes the interface look better
    print(Fore.GREEN + f.renderText('Amity Space Allocation ')).center(10)

    prompt = '(amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> ..."""
        room_type

    @docopt_cmd
    def do_create_person(self, arg):
        """Usage: create_person <fname> <lname> <role> [<accomodation>]  
        """
        listitems()

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>.
        """
        itemid = arg['<file_name>']
        r

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage:print_allocations [<file_name>] """
        itemid = arg['[<file_name>']

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<file_name>]
        """
        itemid = arg['[<file_name>]']
        check_out(itemid)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>

        """
        itemid = arg['<item_id>']
        view(itemid)

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <database_name> 

        """
        search_string = arg['<search_string>']

    @docopt_cmd
    def do_save_state(self, args):
        """Usage: save_state [<database_name>]

        """

        file_name = args['<file_name>']

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    AmitySpaceAllocation().cmdloop()

print(opt)
