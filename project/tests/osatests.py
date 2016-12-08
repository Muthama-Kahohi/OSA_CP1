import unittest
from app.Amity import Amity, Rooms


class OfficeSpaceAllocationTests(unittest.TestCase):

    def setUp(self):
        self.facility = Amity()
        self.room = Rooms()

    def test_create_single_office(self):
        '''Tests creating a single office room'''
        self.assertEqual(0, self.facility.rooms_list)
        self.facility.create_room(
            {"room_type": "office", "room_name": "Krypton"})
        self.assertEqual(1, len(self.facility.rooms_list))

    def test_create_single_living_room(self):
        ''''Tests creating a single living space'''
        self.assertEqual(0, self.facility.rooms_list)
        self.facility.create_room(
            {"room_type": "living space", "room_name": "PHP"})
        self.assertEqual(1, len(self.facility.rooms_list))

    def test_create_multiple_offices(self):
        self.assertEqual(0, self.facility.rooms_list)
        self.facility.create_room(
            {"room_type": "offices",
                "room_name": ["Hogwarts", "Bumblebee", "Cyan"]})
        self.assertEqual(3, len(self.facility.rooms_list))

    def test_create_multiple_living_spaces(self):
        self.assertEqual(0, self.facility.rooms_list)
        self.facility.create_room(
            {"room_type": "living space",
                "room_name": ["Java", "Python", "Android"]})
        self.assertEqual(3, len(self.facility.rooms_list))

    def test_create_person(self):
        '''Asserts that person is added to a list and they are in the list'''

        s_fname = "Percila"
        f_fname = "Paul"
        self.assertEqual(0,
                         len(self.facility.persons_list))
        self.facility.create_person(f_fname, "Kahohi", "Fellow", "Y")
        self.facility.create_person(s_fname, "Njira", "Staff", "N")
        self.assertEqual(2,
                         len(self.facility.persons_list))
        self.assertIn(s_fname, self.facility.persons_list)
        self.assertIn(f_fname, self.facility.persons_list)        


    def test_person_values_added_are_of_correct_types(self):

        self.assertEqual(0,
                        len(self.facility.persons_list))
        self.assertRaises(ValueError,
            self.facility.create_person,456, "Muthama", "Fellow","Y" )
        self.assertRaises(ValueError,
            self.facility.create_person,"Paul", 89, "Fellow","Y" )
        self.assertRaises(ValueError,
            self.facility.create_person,"percila", "Njira", 768,"Y" )
        self.assertRaises(ValueError,
            self.facility.create_person,"Percila", "Njira", "Fellow", 0 )     

    def test_add_person_to_room(self):
        r_name = "PHP"
        f_fname = "Paul"
        self.facility.create_person(f_fname, "Kahohi", "Fellow", "Y")        
        self.facility.create_room(
            {"room_type": "living space", "room_name": r_name})
        # self.assertEqual(1, len(self.facility.rooms_list))
        r_name = self.room
        self.assertEqual(0,len(self.room.occupants))
        self.facility.add_person(r_name, f_fname)
        self.assertEqual(1,len(self.room.occupants))


    def test_reallocate(self):
        '''
        1. create person
        2. create room
        3. remove person from room
        4. confirm person removed from room
        5. Add person to another room
        6. confirm person is added to that particular room
        '''


if __name__ == '__main__':
    unittest.main()
