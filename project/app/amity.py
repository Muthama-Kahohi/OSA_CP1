
from random import randint
from people import Person, Staff, Fellow
import random
import uuid
from db.db_manager import AmityRooms, Persons, create_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text, select
from termcolor import colored
import os.path


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
        self.rooms_from_db = []
        self.room_names_list = []

    def create_room(self, to_create={}):
        if 'room_type' in to_create.keys() and 'room_name' in to_create.keys():
            room_type = to_create['room_type'].lower()
            print(room_type)
            if room_type == 'office':
                
                if type(to_create['room_name']) is list:

                    for item in to_create['room_name']:
                        room_name = item.lower()
                        if room_name not in self.room_names_list:
                            self.office_list.append(
                                {'room_name': room_name, 'room_type': room_type, "occupants": []})
                            self.rooms_list.append(room_name)
                            self.unfilled_offices.append(room_name)
                            self.room_names_list.append(room_name)
                            print(colored("%s has been created sucessfully" % room_name,"green"))
                            # room_name = Office(room_name)
                        else:
                            print (colored("%s already exists" %room_name, "red")).center(70)                
                else:
                    to_create['room_name'] = str(to_create['room_name']).lower()
                    if type(to_create['room_name']) is str:
                        room_name = to_create['room_name']
                        if room_name not in self.room_names_list:
                            self.office_list.append(
                                {'room_name': room_name, 'room_type': room_type,
                                    "occupants": []})
                            self.rooms_list.append(room_name)
                            self.unfilled_offices.append(room_name)
                            self.room_names_list.append(room_name)
                            print(colored("%s has been created sucessfully" % room_name,"green")).center(70)
                            # room_name = Office(room_name)

                        else:
                            print (colored("Room already exists", "red"))

            elif room_type == 'living':
                
                if type(to_create['room_name']) is list:
                    
                    for item in to_create['room_name']:
                        room_name = item.lower()
                        if room_name not in self.room_names_list:
                            self.living_list.append(
                                {'room_name': room_name, 'room_type': room_type, "occupants": []})
                            self.rooms_list.append(room_name)
                            self.unfilled_living.append(room_name)
                            self.room_names_list.append(room_name)
                            print(colored("%s has been created sucessfully" % room_name,"green"))
                            # room_name = Office(room_name)
                        else:
                            print (colored("%s already exists" %room_name, "red")).center(70)                
                else:
                    to_create['room_name'] = str(to_create['room_name']).lower()
                    if type(to_create['room_name']) is str:
                        room_name = to_create['room_name']
                        if room_name not in self.room_names_list:
                            self.living_list.append(
                                {'room_name': room_name, 'room_type': room_type,
                                    "occupants": []})
                            self.rooms_list.append(room_name)
                            self.unfilled_living.append(room_name)
                            self.room_names_list.append(room_name)
                            print(colored("%s has been created sucessfully" % room_name,"green")).center(70)
                            # room_name = Office(room_name)

                        else:
                            print (colored("Room already exists", "red"))

            else:
                print(colored("Room can only be an Office or a Living Space", "red")).center(70)
        self.rooms_list = self.office_list + self.living_list

    def room_availability(self):
        for room in self.office_list:
            if len(room['occupants']) == 6:
                filled_room = room['room_name']
                # print("Room %s is full. Removing from vacant rooms"
                #       % filled_room)
                if filled_room in self.unfilled_offices:
                    self.unfilled_offices.remove(filled_room)
                else:
                    continue    
        for room in self.living_list:
            if len(room['occupants']) == 4:
                room_name = room['room_name']
                # print("Room %s is full. Removing from vacant rooms"
                #       % room_name)
                if room_name in self.unfilled_living:
                    self.unfilled_living.remove(room_name)
                else:
                    continue    
        print("Room availability check done************")

    def create_person(self, fname, lname, role, accomodation = 'N'):
        role = role.upper()
        fellow, staff, yes, no = 'FELLOW', 'STAFF', 'Y', 'N'
        # Ensure that the  first name and last name are strings
        try:
            if type(fname) is not str or type(lname) is not str:
                print("The names should be of type string").center(70)
                raise ValueError
                return
            # Ensures that invalid roles are not added
            if role != fellow and role != staff:
                print("Role can only be either a fellow or a staff").center(70)
                raise ValueError
                return
        except ValueError:
            print(colored("Invalid values. Please try again", "red")).center(70)
            return        
        # Ensure that accomoadation can only be Y or N
        try:
            if type(accomodation) is not str and type(accomodation) is not str:
                raise TypeError
                print("Invalid accomodation choice").center(70)
                return
            else:
                accomodation = accomodation.upper()            
                if accomodation != yes and accomodation != no:
                    print("Accomodation choice should either be Y or N").center(70)
                    return
                elif role == staff and accomodation == yes:
                    print("Staff members are not given accomodation, only offices").center(70)
                    return
        except TypeError:
            print(colored("Invalid values. Please try again")).center(70) 
            return           
        fnameId = str(uuid.uuid4())[:5:]

        person_dict = {'fname': fname, 'lname': lname,
                       'role': role, 'wants_accomodation': accomodation, 'id': fnameId}

        self.persons_list.append(person_dict)
        
        print (colored("************************************************************", "yellow")).center(70)
        print(colored("%s has been created with id %s" % (fname, fnameId), "blue")).center(70)
        print (colored("************************************************************", "yellow")).center(70)

        # Before allocation room availability is confirrmed
        try:
            self.room_availability()
        except ValueError:
            pass    
        # Allocate office to any person added

        if len(self.unfilled_offices) > 0:
            rand = randint(0, len(self.unfilled_offices) - 1)
            occupy = self.unfilled_offices[rand]
            for room in range(len(self.office_list)):
                if self.office_list[room]['room_name'] == occupy:
                    self.office_list[room]['occupants'].append(fnameId)
                    print(colored("%s has been added to %s" %
                          (fname, self.office_list[room]['room_name']), "blue")).center(70)
                    self.allocated_persons.append(fname)
                    break
                else:
                    continue
        else:
            self.unallocated_persons.append(
                {'fname': fname, 'lname': lname, 'Lacks': 'Office'})
            print(colored("No offices to allocate","red")).center(70)

        if role == fellow and accomodation == yes:
            if len(self.unfilled_living) > 0:
                rand = randint(0, len(self.unfilled_living) - 1)
                occupy = self.unfilled_living[rand]
                for room in range(len(self.living_list)):
                    if self.living_list[room]['room_name'] == occupy:
                        self.living_list[room]['occupants'].append(fnameId)
                        print(colored("%s has been added to %s" %
                              (fname, self.living_list[room]['room_name']), "blue")).center(70)
                        break
                    else:
                        continue
            else:
                self.unallocated_persons.append(
                    {'fname': fname, 'lname': lname, 'Lacks': 'Living space'})

                print(colored("No Living space to allocate","red")).center(70)


    def return_office_name(self, id):
        '''returns the name of the office in which a particular id is in'''
        found = False
        for room in range(len(self.office_list)):
            if id not in self.office_list[room]['occupants']:
                continue
            else:
                ron = self.office_list[room]['room_name']
                found = True
        if found:
            return ron
        else:
            return 'None'

    def return_living_name(self, id):
        found = False
        for room in range(len(self.living_list)):
            if id not in self.living_list[room]['occupants']:
                continue
            else:
                rln = self.living_list[room]['room_name']
                found = True
        if found:
            return rln
        else:
            return 'None'

    def reallocate(self, occupant_id, room_to):
        found = False
        str(occupant_id)
        room_to = room_to.lower()
        # Ensure that a member is reallocated to an unfilled room
        if room_to in self.room_names_list:
            self.room_availability()
            vacant_rooms = self.unfilled_living + self.unfilled_offices
            if room_to in vacant_rooms:
                
                for room in self.office_list:
                    if room['room_name'] == room_to:
                        found = True
                        room['occupants'].append(occupant_id)
                        print(colored("Succesfully reallocated to %s" %room['room_name'], "green"))
                        break
                    else:
                        continue
                if found:        
                    for room in self.office_list:
                        if occupant_id in room['occupants'] and room['room_name'] != room_to:
                            room['occupants'].remove(occupant_id)
                            print(colored(" % s removed from % s" 
                                  %(occupant_id, room['room_name']), "red"))
                            return
                        else:
                            continue        
            

                for room in self.living_list:
                    if room['room_name'] == room_to:
                        room['occupants'].append(occupant_id)
                        print(colored("Succesfully reallocated to %s" %room['room_name'], "green"))
                        break
                    else:
                        continue
                for room in self.living_list:
                    if occupant_id in room['occupants'] and room['room_name'] != room_to:
                        room['occupants'].remove(occupant_id)
                        print(colored(" % s removed from % s" 
                              %(occupant_id, room['room_name']), "red"))
                        return
                    else:
                        continue        
            else:
                print (colored("That room is already full and cannot be added","red"))
        else:
            print(colored("No such room exists", "red"))        

    def print_room(self, room_name):
        if room_name in self.room_names_list:    
            print(colored("---------------------------------------------------", "white")).center(70) 
            print(colored(room_name.upper(), "green")).center(70)
            print(colored("---------------------------------------------------", "white")).center(70)
        
            for room in self.office_list:
                if room_name == room['room_name']:
                    if len(room['occupants']) > 0:
                        for occupant in room['occupants']:
                            print(colored(self.return_names(occupant), "white")).center(70)
                        break
                    else:
                        print(colored("No occupants", "red")).center(70)
                else:
                    continue

            for room in self.living_list:
                if room_name == room['room_name']:
                    if len(room['occupants']) > 0:
                        for occupant in room['occupants']:
                            print(colored(self.return_names(occupant), "white")).center(70)
                        break
                    else:
                        print(colored("No occupants", "red")).center(70)
                else:
                    continue
        else:
            print(colored("No such room exists", "red"))            

    def return_names(self, id):
        print(id)
        for person in range(len(self.persons_list)):
            if self.persons_list[person]['id'] == id:
                fname = self.persons_list[person]['fname']
                lname = self.persons_list[person]['lname']
                break
            else:
                continue
        return('%s %s' % (fname, lname))

    def load_people(self, file_name):
        if  not os.path.isfile(file_name):
            print("File does not exist")
        else:    
            array = []
            print(colored("LOADING"))
            try:
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
            except IOError:
                print(colored("%s does not exist" %file_name, "red"))            

    def print_allocations(self, file_name=None):
        self.file_name= file_name
        if self.file_name is None:
            for room in range(len(self.rooms_list)):
                print(colored("-------------------------------------------", "white"))
                print(colored(self.rooms_list[room]['room_name'].upper(), "green"))
                print(colored("-------------------------------------------", "white"))
                if self.rooms_list[room]['occupants'] > 1:
                    for occupant in self.rooms_list[room]['occupants']:
                        print(colored(self.return_names(occupant), "yellow"))

        else:
            with open(self.file_name, mode='w') as ins:
                for room in range(len(self.rooms_list)):
                    ins.write(
                        '--------------------------------------------------\n')
                    ins.write(self.rooms_list[room][
                              'room_name'].upper() + '\n')
                    ins.write(
                        '----------------------------------------------------\n')
                    if self.rooms_list[room]['occupants'] > 1:
                        for occupant in self.rooms_list[room]['occupants']:
                            ins.write(self.return_names(occupant) + " ")
                    


    def print_unallocated(self, file_name=None):
        self.file_name =file_name
        if self.file_name is None:
            print("Persons Unallocated offices")
            print('-') * 50
            for person in range(len(self.unallocated_persons)):
                if self.unallocated_persons[person]['Lacks'] == "Office":
                    print(self.unallocated_persons[person][
                          'fname'] + ' ' + self.unallocated_persons[person]['lname'])
            print("Persons Unallocated Living Spaces")
            print('-') * 50
            for person in range(len(self.unallocated_persons)):
                if self.unallocated_persons[person]['Lacks'] == "Living space":
                    print(self.unallocated_persons[person][
                          'fname'] + ' ' + self.unallocated_persons[person]['lname'])

        else:
            with open(self.file_name, mode='w') as ins:
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
                print(colored("%s created. Check Your directory " %file_name ,"green"))       

    def save_state(self, db_name='amity'):
        engine = create_db(db_name)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()
        # Selects all the items in the Rooms table
        items = select([AmityRooms])
        result = session.execute(items)
        dbrooms_list = [item.room_name for item in result]
        for room in range(len(self.rooms_list)):
            if self.rooms_list[room]['room_name'] not in dbrooms_list:
                new_room = AmityRooms(room_name=self.rooms_list[room]['room_name'],
                                      room_type=self.rooms_list[room]['room_type'])
                session.add(new_room)
                session.commit()


        andelans = select([Persons])
        response = session.execute(andelans)
        dbpersons_list = [item.andela_id for item in response]

        for andelan in range(len(self.persons_list)):
            idk = self.persons_list[andelan]['id']
            if idk not in dbpersons_list:
                officename = self.return_office_name(idk)
                livingname = self.return_living_name(idk)
                fname = self.persons_list[andelan]['fname']
                lname = self.persons_list[andelan]['lname']
                role = self.persons_list[andelan]['role']
                accomodation = self.persons_list[andelan]['wants_accomodation']
                new_person = Persons(fname=fname,
                                     lname=lname,
                                     role=role,
                                     accomodation=accomodation,
                                     andela_id=idk,
                                     office_allocated=officename,
                                     living_allocated=livingname)
                session.add(new_person)
                session.commit()
        print(colored("Application data successfully saved to the database >> %s" %db_name, "red"))        

    def load_state(self, db_name):
        if not os.path.isfile(db_name):
            print("Database does not exist")
        else:    
            # create engine
            engine = create_engine('sqlite:///' + db_name)
            # Bind engine to Base Metadata
            Base.metadata.bind = engine
            # creates session
            Session = sessionmaker(bind=engine)
            session = Session()

            # Selects all the rooms in the Rooms table
            items = select([AmityRooms])
            result = session.execute(items)

            # orders the result to enable  tabulation
            for item in result.fetchall():
                name = item.room_name
                rtype = item.room_type
                
                if  rtype == 'office':
                    if len(self.office_list) == 0:
                        self.create_room({"room_type":'office', "room_name":name})
                    else:
                        for room in self.office_list:
                            if name not in self.room_names_list:
                                self.create_room({"room_type":'office', "room_name":name})
                else:
                    if len(self.living_list) == 0:
                        self.create_room({"room_type":'living', "room_name":name}) 
                    else:                   
                        for room in self.living_list:
                            if name not in self.room_names_list:  
                                self.create_room({"room_type":'living', "room_name":name})
            session.close()

            # Selects all the rooms in the Rooms table
            items = select([Persons])
            result = session.execute(items)

            # orders the result to enable  tabulation
            for item in result.fetchall():
                fname = item.fname
                lname = item.lname
                role = item.role
                accomodation = item.accomodation
                andela_id = item.andela_id
                office_allocated = item.office_allocated
                living_allocated = item.living_allocated
                
                if  len(self.persons_list) == 0:
                    self.persons_list.append(
                        {'fname':fname,'lname':lname,'role':role ,'wants_accomodation':accomodation, 'id':andela_id})
                    for room in self.office_list:
                        if office_allocated == room['room_name']:
                            if  andela_id not in room['occupants']:
                                room['occupants'].append(andela_id)
                            else:
                                continue    
                    for room in self.living_list:
                        if living_allocated == room['room_name']:
                            if andela_id not in room['occupants']: 
                                room['occupants'].append(andela_id)
                            else:
                                continue    
                else:
                    for person in self.persons_list:
                        if andela_id not in person['id']:
                            continue
                        else:
                            print(colored("%s already exists" %fname, "red"))
                            break                               
                    self.persons_list.append(
                        {'fname':fname,'lname':lname,'role':role ,'wants_accomodation':accomodation, 'id':andela_id})
                    for room in self.office_list:
                        if office_allocated == room['room_name']:
                            if  andela_id not in room['occupants']:
                                room['occupants'].append(andela_id)
                            else:
                                continue    
                    for room in self.living_list:
                        if living_allocated == room['room_name']:
                            if andela_id not in room['occupants']: 
                                room['occupants'].append(andela_id)
                            else:
                                continue

                
            self.unfilled_offices = [self.office_list[room]['room_name'] for room in range(len(self.office_list)) if len(self.office_list[room]['occupants']) < 6] 
            self.unfilled_living = [self.living_list[room]['room_name'] for room in range(len(self.living_list)) if len(self.living_list[room]['occupants']) < 4]
            self.room_list = self.office_list + self.living_list

            session.close()
            print(colored("Data successfuly added to the application", "green"))



class Rooms (object):

    def __init__(self):
        self.occupants = []


class LivingSpace(Rooms):
    def _init__(self):
        self.capacity = 4        
    


class Office(Rooms):
    def _init__(self):
        self.capacity = 6

