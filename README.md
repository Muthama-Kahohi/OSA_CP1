# Amity Office Space Allocation
##Introduction
A command line application that allocates offices and living spaces to fellows and staff.

##Features
1. **add_person <fname> <lname> <role> <wants_accomodation>** .... Adds either a staff or a fellow. The deafult value for <wants_accomodation> is No.
2. **create_room <room_type> <room_name>** ... creates a room with the type either being an office or a living space. Command also allows adding of multiple rooms.
3. **load_people <file_name>** .... adds people from a text file.
4. **save_state [--db=sqlite_database]** ... Persists all the data stored in the app to a SQLite database. Specifying the --db parameter   explicitly stores the data in the sqlite_database specified.  
5. **load_state <sqlite_database>** - Loads data from a database into the application.
6. **reallocate_person <person_identifier> <new_room_name>** ... Reallocate the person with person_identifier to new_room_name.
7. **print_allocations [filename]** ... Prints a list of allocations onto the screen. Specifying the optional file_name option here outputs the registered allocations to a txt file.
8. **print_unallocations [filename]** ... Prints a list of unallocated persons onto the screen. Specifying the optional file_name option here outputs the registered allocations to a txt file
9. **print_room <room_name>** ... Prints  the names of all the people in room_name on the screen.


##Installation:
1. git clone [repo](https://github.com/Muthama-Kahohi/OfficeSpaceAllocation_CP1.git)
2. create a virtualenv `virtualenv venv`
3. Install requirements `pip install -r requirements`
4. Run command to enter `python amity_init.py -i`
5. `help` to get list of commands

##Core Dependencies	
###[docopt](http://docopt.org/)
Defines interface for command line app and automatically generates parser

###[pyfiglet](https://pypi.python.org/pypi/pyfiglet)
Defines font for texts appearing on interface

###[colorama](https://pypi.python.org/pypi/colorama)
Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request 