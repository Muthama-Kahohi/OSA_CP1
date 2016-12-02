import unittest
from app.amity import Amity, Rooms, LivingSpace, Office
from app.people import Person, Fellow, Staff


class OfficeSpaceAllocationTests(unittest.TestCase):

    def setUp(self):
        self.facility = Amity()
        # self.room=Rooms()
        self.space = LivingSpace()
        self.office = Office()
        self.Person = Person()
        self.fellow = Fellow()
        self.staff = Staff()

    # First four tests test for inheritance
    def test_LivingSpace_child_of_Rooms(self):
        self.assertIsInstance(self.space, Rooms)

    def test_Office_child_of_Rooms(self):
        self.assertIsInstance(self.office, Rooms)

    def test_Fellow_child_of_Person(self):
        self.assertIsInstance(self.fellow, Person)

    def test_Staff_child_of_Person(self):
        self.assertIsInstance(self.staff, Person)

    # Tests for Amity class methods
    def test_room_name_is_a_string(self):
        facility = Amity()
        self.assertRaises(TypeError, facility.create_room, 123, 345, "paul")

if __name__ == '__main__':
    unittest.main()
