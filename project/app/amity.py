class Amity(object):

    def __init__(self):
        self.rooms = {}
        self.rooms_list = []
        self.office_list = []
        self.living_list = []
        self.persons_list = []
        self.allocated_persons = []
        pass

    def create_room(self, *args):
        pass

    def create_person(self, *args):
        pass

    def add_person(self,room_name, person_name):
        pass

    def remove_person(self, person_name):
        pass         


class Rooms (object):

    def __init__(self):
        self.occupants = []


        


class LivingSpace(Rooms):
    capacity = 4
        


class Office(Rooms):
    
    capacity = 6
