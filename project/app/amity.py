from random import randint
from people import Person, Staff, Fellow
import random
import uuid


class Amity(object):

    def __init__(self):
        self.rooms = {}
        self.rooms_list = []
        self.office_list = []
        self.living_list = []
        self.persons_list = []
        self.allocated_persons = []
        self.unfilled_offices = []
        self.unfilled_living = []
        self.unallocated_persons = []

    def create_room(self, to_create={}):
        if 'room_type' in to_create.keys() and 'room_name' in to_create.keys():
            room_type = to_create['room_type'].lower()

            if room_type == 'office':
                if type(to_create['room_name']) is str:
                    room_name = to_create['room_name']
                    if room_name not in self.office_list:
                        self.office_list.append(
                            {'room_name': room_name, "occupants": []})
                        self.rooms_list.append(room_name)
                        self.unfilled_offices.append(room_name)
                        room_name = Office(room_name)

                    else:
                        print ("Room already exists")

                elif type(to_create['room_name']) is list:
                    for item in to_create['room_name']:
                        room_name = item
                        if room_name not in self.office_list:
                            self.office_list.append(
                                {'room_name': room_name, "occupants": []})
                            self.rooms_list.append(room_name)
                            self.unfilled_offices.append(room_name)
                            room_name = Office(room_name)

                        else:
                            print("Room already exists")

            elif room_type == 'living':
                if type(to_create['room_name']) is str:
                    room_name = to_create['room_name']
                    if room_name not in self.living_list:
                        self.living_list.append(
                            {'room_name': room_name, "occupants": []})
                        self.rooms_list.append(room_name)
                        self.unfilled_living.append(room_name)
                        room_name = LivingSpace(room_name)
                        print(self.unfilled_living)
                        print('The rooms capacity is:%d ' % room_name.capacity)
                    else:
                        print("Room already exists")

                elif type(to_create['room_name']) is list:
                    for item in to_create['room_name']:
                        room_name = item
                        if room_name not in self.living_list:
                            self.living_list.append(
                                {'room_name': room_name, 'occupants': []})
                            self.rooms_list.append(room_name)
                            self.unfilled_living.append(room_name)
                            room_name = LivingSpace(room_name)
                        else:
                            print("Room already exists")

            else:
                print("Room can only be an Office or a Living Space")
        self.rooms_list = self.office_list + self.living_list

    def room_availability(self):
        for room in range(len(self.office_list)):
            if len(self.office_list[room]['occupants']) == 6:
                filled_room = self.office_list[room]['room_name']
                print("Room %s is full. I t has to be removed++++++++++++++"
                      % filled_room)
                self.unfilled_offices.remove(filled_room)
        for room in range(len(self.living_list)):
            if len(self.living_list[room]['occupants']) == 4:
                room_name = self.living_list[room]['room_name']
                print("Room %s is full. I t has to be removed++++++++++++++"
                      % room_name)
                self.unfilled_living.remove(room_name)
        print("Room availability check done************")

    def create_person(self, fname, lname, role, accomodation):
        role, accomodation = role.upper(), accomodation.upper()
        fellow, staff, yes, no = 'FELLOW', 'STAFF', 'Y', 'N'
        # Ensure that the  first name and last name are strings
        if type(fname) is not str or type(lname) is not str:
            print("The names should be of type string")
            return
        # Ensures that invalid roles are not added
        if role != fellow and role != staff:
            print("Role can only be either a fellow or a staff")
            return
        # Ensure that accomoadation can only be Y or N
        if type(accomodation) is not str and type(accomodation) is not str:
            raise TypeError
            print("Invalid accomodation choice")
            return
        else:
            if accomodation != yes and accomodation != no:
                print("Accomodation choice should either be Y or N")
                return
            elif role == staff and accomodation == yes:
                print("Staff members are not given accomodation, only offices")
                return
        # Generate a unique id for every person created
        fname = Person(fname)
        fnameId = uuid.uuid4()

        person_dict = {'fname': fname.fname, 'lname': lname,
                       'role': role, 'wants_accomodation': accomodation, 'id': fnameId}

        self.persons_list.append(person_dict)
        print (person_dict)
        print ('%s has been created with id %d.' %
               (fname.fname, fnameId))
        # Before allocation room availability is confirrmed
        self.room_availability()
        # Allocate office to any person added

        if len(self.unfilled_offices) > 0:
            rand = randint(0, len(self.unfilled_offices) - 1)
            occupy = self.unfilled_offices[rand]
            for room in range(len(self.office_list)):
                if self.office_list[room]['room_name'] == occupy:
                    self.office_list[room]['occupants'].append(fnameId)
                    print("%s has been added to %s" %
                          (fname.fname, self.office_list[room]['room_name']))
                    break
                else:
                    continue
        else:
            self.unallocated_persons.append(
                {'fname': fname.fname, 'lname': lname, 'Lacks': 'Office'})
            print("No offices to allocate")

        if role == fellow and accomodation == yes:
            if len(self.unfilled_living) > 0:
                rand = randint(0, len(self.unfilled_living) - 1)
                occupy = self.unfilled_living[rand]
                for room in range(len(self.living_list)):
                    if self.living_list[room]['room_name'] == occupy:
                        self.living_list[room]['occupants'].append(fnameId)
                        print("%s has been added to %s" %
                              (fname.fname, self.living_list[room]['room_name']))
                        print(self.unfilled_living)
                        break
                    else:
                        continue
            else:
                self.unallocated_persons.append(
                    {'fname': fname.fname, 'lname': lname, 'Lacks': 'Living space'})

                print("No Living space to allocate")

    def remove_person(self, person_name):
        pass

    def reallocate(self, id, room_to):
        for room in range(len(self.office_list)):
            for occupant in range(len(self.office_list[room]['occupants'])):
                if occupant == id:
                    self.office_list[room]['occupants'].remove(id)
                    break
                else:
                    continue
        for room in range(len(self.living_list)):
            for occupant in range(len(self.living_list[room]['occupants'])):
                if occupant == id:
                    self.office_list[room]['occupants'].remove(id)
                    break
                else:
                    continue
        # Ensure that a member is reallocated to an unfilled room
        vacant_rooms = self.unfilled_living + self.unfilled_offices
        if room_to in vacant_rooms:
            for room in range(len(self.office_list)):
                if self.office_list[room]['room_name'] == room_to:
                    self.office_list[room]['occupants'].append(id)
                    break
                else:
                    continue

            for room in range(len(self.living_list)):
                if self.living_list[room]['room_name'] == room_to:
                    self.living_list[room]['occupants'].append(id)
                    break
                else:
                    continue
        else:
            print "That room is already full and cannot be added"

    def print_room(self, room_name):
        print("x") * 60
        print(room_name.upper())
        print("x") * 60
        for room in range(len(self.office_list)):
            if room_name == self.office_list[room]['room_name']:
                if len(self.office_list[room]['occupants']) > 1:
                    for occupant in self.office_list[room]['occupants']:
                        print(self.return_names(occupant))
                    break
                else:
                    print("No occupants")
            else:
                continue

        for room in range(len(self.living_list)):
            if room_name == self.living_list[room]['room_name']:
                if len(self.living_list[room]['occupants']) > 1:
                    for occupant in self.living_list[room]['occupants']:
                        print(self.return_names(occupant))
                    break
                else:
                    print("No occupants")
            else:
                continue

    def return_names(self, id):
        for person in range(len(self.persons_list)):
            if self.persons_list[person]['id'] == id:
                fname = self.persons_list[person]['fname']
                lname = self.persons_list[person]['lname']
                break
            else:
                continue
        return('%s %s' % (fname, lname))

    def load_people(self, file_name):
        array = []
        with open(file_name, mode="r") as ins:
            array = ins.readlines()
            for persons in array:
                person = persons.split()
                fname = person[0]
                lname = person[1]
                role = person[2]
                if role == 'STAFF' and len(person) == 3:
                    accomodation = 'N'
                else:
                    accomodation = person[3]
                self.create_person(fname, lname, role, accomodation)

    def print_allocations(self, file_name=None):
        if file_name == None:
            for room in range(len(self.rooms_list)):
                print('-') * 50
                print(self.rooms_list[room]['room_name'].upper())
                print('-') * 50
                if self.rooms_list[room]['occupants'] > 1:
                    for occupant in self.rooms_list[room]['occupants']:
                        print(self.return_names(occupant))
        else:
            with open(file_name, mode='w') as ins:
                for room in range(len(self.rooms_list)):
                    ins.write(
                        '--------------------------------------------------\n')
                    ins.write(self.rooms_list[room][
                              'room_name'].upper() + '\n')
                    ins.write(
                        '----------------------------------------------------\n')
                    if self.rooms_list[room]['occupants'] > 1:
                        for occupant in self.rooms_list[room]['occupants']:
                            ins.write(self.return_names(occupant) + ',')

    def print_unallocated(self, file_name=None):
        if file_name == None:
            print("Persons Unallocated offices")
            print('-') * 50
            for person in range(len(self.unallocated_persons)):
                if self.unallocated_persons[person]['Lacks'] == "Office":
                    print(self.unallocated_persons[person][
                          'fname'] + ' ' + self.unallocated_persons[person]['lname'])
            print("Persons Unallocated Living Spaces")
            print('-') * 50
            for person in range(len(self.unallocated_persons)):
                if self.unallocated_persons[person]['Lacks'] == "Living Space":
                    print(self.unallocated_persons[person][
                          'fname'] + ' ' + self.unallocated_persons[person]['lname'])

        else:
            with open(file_name, mode = 'w') as ins:
                ins.write("Persons Unallocated offices\n")
                ins.write('----------------------------\n')
                for person in range(len(self.unallocated_persons)):
                    if self.unallocated_persons[person]['Lacks'] == "Office":
                        ins.write(self.unallocated_persons[person][
                              'fname'] + ' ' + self.unallocated_persons[person]['lname'] + '\n')
                ins.write('------------------------------------------------\n\n')

                ins.write("Persons Unallocated Living Spaces \n")
                ins.write('-----------------------------------\n') 
                for person in range(len(self.unallocated_persons)):
                    if self.unallocated_persons[person]['Lacks'] == "Living Space":
                        ins.write(self.unallocated_persons[person][
                              'fname'] + ' ' + self.unallocated_persons[person]['lname'] + '\n')            

class Rooms (object):

    def __init__(self):
        self.occupants = []


class LivingSpace(Rooms):
    def __init__(self, room_name):
        self.capacity = 4


class Office(Rooms):
    def __init__(self, room_name):
        self.capacity = 6

k = Amity()
# k.create_room({'room_type': "office", "room_name": [
#               'Hogwarts', 'Occulus']})
k.create_room({'room_type': 'living', 'room_name': ['Go']})
k.load_people('file.txt')
k.print_unallocated('new.txt')
