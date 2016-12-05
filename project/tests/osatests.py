import unittest
from app.amity import Amity, Rooms, LivingSpace, Office
from app.people import Person, Fellow, Staff


class OfficeSpaceAllocationTests(unittest.TestCase):

    def setUp(self):
        self.facility = Amity()
        self.room = Rooms()
        self.space = LivingSpace()
        self.office = Office()
        self.Person = Person()
        self.fellow = Fellow()
        self.staff = Staff()

    # First four tests test for inheritance
    def test_create_single_office_room(self):
        '''Tests creating a single office room'''
        self.facility.create_room(
            {"room_type": "office", "room_name": "Krypton"})
        self.assertEqual(1, len(self.facility.rooms_list))

    def test_create_single_living_room(self):
        ''''Tests creating a single living space'''
        self.facility.create_room(
            {"room_type": "living space", "room_name": "PHP"})
        self.assertEqual(1, len(self.facility.rooms_list))

    def test_create_multiple_offices(self):
        self.facility.create_room(
            {"room_type": "offices",
                "room_name": ["Hogwarts", "Bumblebee", "Cyan"]})
        self.assertEqual(3, len(self.facility.rooms_list))

    def test_create_multiple_living_spaces(self):
        self.facility.create_room(
            {"room_type": "living space",
                "room_name": ["Java", "Python", "Android"]})
        self.assertEqual(3, len(self.facility.rooms_list))

    def test_parameters_passed_are_strings(self):
        """Ensures all the parameterts passeds are strings """
        self.assertRaises(
            ValueError, self.facility.create_room, 111, 444, 555)

        self.assertRaises(
            ValueError, self.facility.create_room, "Offices", 444, 555)

    def test_test_room_type_is_livingspace_or_room(self):

        self.facility.create_room(
            {"room_type": "living space",
                "room_name": ["Java", "Python", "Android"]})

        self.assertIn(
            self.facility.rooms_list[0]["room_name"], self.facility.room_type)

    def test_add_person(self):
        '''Test that a person is added'''
        self.facility.add_person(
            {"first_name": "Paul", "second_name": "Kahohi",
             "Title": "Fellow", "wants_accomodation": "Y"})
        self.assertEqual(1, len(self.facility.persons_list))

    def test_person_details_are_strings(self):
        """Ensures the details added are strings"""
        self.assertRaises(ValueError, self.facility.add_person,
                          "paul", 763, "fellow", 1)

        self.assertRaises(ValueError, self.facility.add_person,
                          453, 763, 34, 7)

    def test_person_allocation(self):
            




if __name__ == '__main__':
    unittest.main()
