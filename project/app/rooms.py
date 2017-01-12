class Rooms (object):

    def __init__(self):
        self.occupants = []


class LivingSpace(Rooms):
    def _init__(self):
        self.capacity = 4        
    


class Office(Rooms):
    def _init__(self):
        self.capacity = 6
