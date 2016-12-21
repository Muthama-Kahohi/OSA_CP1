import unittest
from app.Amity import Amity, Rooms, Office, LivingSpace
from app.people import Person, Fellow, Staff


class OfficeSpaceAllocationTests(unittest.TestCase):

    def setUp(self):
        self.facility = Amity()
        self.room = Rooms()
        self.room2 = Rooms()

    def test_create_single_office(self):
        '''Tests creating a single office room'''
        self.assertEqual(0, len(self.facility.rooms_list))
        self.facility.create_room(
            {"room_type": "office", "room_name": "Krypton"})
        num = len(self.facility.rooms_list)
        self.assertEqual(1, num)

    def test_create_single_living_room(self):
        ''''Tests creating a single living space'''
        self.assertEqual(0, len(self.facility.rooms_list))
        self.facility.create_room(
            {"room_type": "living", "room_name": "PHP"})
        self.assertEqual(1, len(self.facility.rooms_list))

    def test_create_multiple_offices(self):
        self.assertEqual(0, len(self.facility.rooms_list))
        self.facility.create_room(
            {"room_type": "office",
                "room_name": ["Hogwarts", "Bumblebee", "Cyan"]})
        self.assertEqual(3, len(self.facility.rooms_list))

    def test_create_multiple_living_spaces(self):
        self.assertEqual(0, len(self.facility.rooms_list))
        self.facility.create_room(
            {"room_type": "living",
                "room_name": ["Java", "Python", "Android"]})
        self.assertEqual(3, len(self.facility.rooms_list))

    def test_create_person(self):
        '''Asserts that person is added to a list and they are in the list'''

        s_fname = "Percila"
        f_fname = "Paul"
        self.assertEqual(0,
                         len(self.facility.persons_list))

        self.facility.create_person(s_fname, "Njira", "Staff", "N")
        self.assertEqual(1,
                         len(self.facility.persons_list))

    def test_person_values_added_are_of_correct_types(self):

        self.assertEqual(0,
                         len(self.facility.persons_list))
        self.assertRaises(ValueError,
                          self.facility.create_person, 456, "Muthama", "Fellow", "Y")
        self.assertRaises(ValueError,
                          self.facility.create_person, "Paul", 89, "Fellow", "Y")
        self.assertRaises(TypeError,
                          self.facility.create_person, "Percila", "Njira", "Fellow", 0)

    def test_add_person_to_room(self):
        r_name = "PHP"
        f_fname = "Paul"
        self.assertEqual(0, len(self.facility.allocated_persons))
        self.facility.create_room(
            {"room_type": "living", "room_name": r_name})
        self.facility.create_room(
            {"room_type": "office", "room_name": 'krypton'})
        self.facility.create_person(f_fname, "Kahohi", "Fellow", "Y")

        self.assertEqual(1, len(self.facility.allocated_persons))

    def test_reallocate(self):
        r_name = "Go"
        r2_name = "Java"
        f_fname = "Sophie"
        self.facility.create_person(f_fname, "Kahohi", "Fellow", "Y")
        self.facility.create_room(
            {"room_type": "living", "room_name": r_name})
        self.facility.create_room(
            {"room_type": "living", "room_name": r2_name})
        # self.assertEqual(1, len(self.facility.rooms_list))

        self.assertEqual(0, len(self.room.occupants))
        self.assertEqual(0, len(self.room2.occupants))

        # Adds person to room
        self.facility.add_person(self.room2, f_fname)
        self.assertEqual(1, len(self.room2.occupants))

        # Reallocate person
        self.reallocate(f_fname, self.room2, self.room)
        self.assertEqual(1, len(self.room.occupants))
        self.assertEqual(0, len(self.room2.occupants))

    def test_maximum_capacities_of_room_and_office(self):
        living = LivingSpace("Shell")
        office = Office("Camelot")
        self.assertEqual(4, living.capacity)
        self.assertEqual(6, office.capacity)

    def test_room_availability(self):
        '''test that only unfilled rooms are available for allocation'''
        self.facility.create_room({"room_type": "living", "room_name": 'Go'})
        living = LivingSpace('Go')
        self.assertEqual(1, len(self.facility.unfilled_living))
        self.facility.create_person('paul', "Kahohi", "Fellow", "Y")
        self.facility.create_person('sophie', "Kibanani", "Fellow", "Y")
        self.facility.create_person('victor', "wabwoba", "Fellow", "Y")
        self.facility.create_person('Madeline', "Kwambok", "Fellow", "Y")
        self.assertEqual(4, len(self.facility.living_list[0]['occupants']))
        self.facility.room_availability()
        self.assertEqual(0, len(self.facility.unfilled_living))

    def test_return_office_name(self):
        self.facility.create_room({"room_type": "office", "room_name": 'Go'})
        self.facility.create_person('paul', "Kahohi", "Fellow", "N")
        fid = self.facility.persons_list[0]['id']
        self.assertEqual('Go', self.facility.return_office_name(fid))

    def test_return_living_name(self):
        self.facility.create_room({"room_type": "living", "room_name": 'Go'})
        self.facility.create_person('paul', "Kahohi", "Fellow", "Y")
        fid = self.facility.persons_list[0]['id']
        self.assertEqual('Go', self.facility.return_living_name(fid))        



if __name__ == '__main__':
    unittest.main()
