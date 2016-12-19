from random import randint
from people import Person, Staff, Fellow


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
        #Generate a unique id for every person created        
        fname = Person(fname)
        fnameId = id(fname)

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
                print("No Living space to allocate")

    def remove_person(self, person_name):
        pass

    def reallocate(self, id, room_from, room_to):
        for room in range(len(self.office_list)):
            if self.office_list[room]['room_name'] == room_from:
                self.office_list[room]['occupants'].remove(id)
                break
            else:
                continue

        for room in range(len(self.living_list)):
            if self.living_list[room]['room_name'] == room_from:
                self.living_list[room]['occupants'].remove(id)
                break
            else:
                continue
        #Ensure that a member is reallocated to an unfilled room  
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
k.create_room(
    {'room_name': ['Hogwarts', 'Krypton', 'Occulus'], 'room_type': 'office'})
k.create_room({'room_name': ['Go', 'pearl', 'Arduino'], 'room_type': 'living'})
k.create_person("paul", "Muthama", 'Fellow', 'Y')
k.create_person("awesome", "Muthama", 'Fellow', 'Y')
k.create_person("sxjhjshn", "Muthama", 'Fellow', 'Y')
k.create_person("bxjhhj", "Muthama", 'Fellow', 'Y')
k.create_person("Ibrahim", "Machela", 'Fellow', 'Y')

k.reallocate(4441238544, 'Occulus', 'Krypton')
