# Amity Office Space Allocation
##Introduction
A command line application that allocates offices and living spaces to fellows and staff.

##Features
1. add_person
2. create_room
3. load_people
4. save_state
5. load_state
6. reallocate
7. print_allocations
8. print_unallocations
9. print_room

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