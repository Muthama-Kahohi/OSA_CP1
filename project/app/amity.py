from random import randint


class Amity(object):

    def __init__(self):
        self.rooms = {}
        self.rooms_list = []
        self.office_list = []
        self.living_list = []
        self.persons_list = []
        self.allocated_persons = []
        self.unfilled_rooms = []

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
                        self.unfilled_rooms.append(room_name)
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
                            self.unfilled_rooms.append(room_name)
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
                        self.unfilled_rooms.append(room_name)
                        room_name = LivingSpace(room_name)
                        print(self.unfilled_rooms)
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
                            room_name = LivingSpace(room_name)
                            self.unfilled_rooms.append(room_name)
                        else:
                            print("Room already exists")

            else:
                print("Room can only be an Office or a Living Space")
        self.rooms_list = self.office_list + self.living_list 

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

        person_dict = {'fname': fname, 'lname': lname,
                       'role': role, 'wants_accomodation': accomodation}

        self.persons_list.append(person_dict)

        print ('%s %s has been added.' % (fname, lname))
        # Allocate office to any person added
        if len(self.office_list) == 1:
            self.office_list[0]['occupants'].append(fname)
            print("%s has been added to %s" %
                  (fname, self.office_list[0]['room_name']))
        elif len(self.office_list) == 0:
            print("No rooms to allocate")
        else:
            rand = randint(0, len(self.office_list) - 1)
            self.office_list[rand]['occupants'].append(fname)
            print("%s has been added to %s" %
                  (fname, self.office_list[rand]['room_name']))
        #Allocate Living Space
        if role == fellow and accomodation == yes:
            if len(self.living_list) == 1:
                self.living_list[0]['occupants'].append(fname)
                print("%s has been added to %s" %
                      (fname, self.living_list[0]['room_name']))
            elif len(self.living_list) == 0:
                print("No rooms to allocate")
            else:
                rand = randint(0, len(self.office_list) - 1)
                self.living_list[rand]['occupants'].append(fname)
                print("%s has been added to %s" %
                      (fname, self.living_list[rand]['room_name']))

    def add_person(self, fname, lname):
        pass            

    def remove_person(self, person_name):
        pass
    def reallocate(self, fname, room_name):
        pass    

    def room_availability(self):
          pass    


class Rooms (object):

    def __init__(self):
        self.occupants = []


class LivingSpace(Rooms):
    def __init__(self, room_name):
        self.capacity = 4


class Office(Rooms):
    def __init__(self, room_name):
        self.capacity = 6


