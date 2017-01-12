class Person(object):
    def __init__(self):
        self.office_allocated = ""


class Fellow(Person):
    def __init__(self):
        self.living_accomodation = "N"


class Staff(Person):
    def __init__(self):
        self.living_accomodation = ""
