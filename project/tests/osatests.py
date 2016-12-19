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


    def test_remove_person(self):
        self.assertEqual(0,
                         len(self.facility.persons_list))
        k = self.facility.create_person("Ian", "Oti", "Fellow", "Y")
        self.assertEqual(1,
                         len(self.facility.persons_list))
        self.facility.remove_person(k)
        self.assertEqual(0,
                         len(self.facility.persons_list))

    def test_person_values_added_are_of_correct_types(self):

        self.assertEqual(0,
                         len(self.facility.persons_list))
        self.assertRaises(ValueError,
                          self.facility.create_person, 456, "Muthama", "Fellow", "Y")
        self.assertRaises(ValueError,
                          self.facility.create_person, "Paul", 89, "Fellow", "Y")
        self.assertRaises(ValueError,
                          self.facility.create_person, "percila", "Njira", 768, "Y")
        self.assertRaises(ValueError,
                          self.facility.create_person, "Percila", "Njira", "Fellow", 0)

    def test_add_person_to_room(self):
        r_name = "PHP"
        f_fname = "Paul"
        self.facility.create_person(f_fname, "Kahohi", "Fellow", "Y")
        self.facility.create_room(
            {"room_type": "living", "room_name": r_name})
        # self.assertEqual(1, len(self.facility.rooms_list))
        self.assertEqual(0, len(self.facility.allocated_persons))
        self.facility.add_person(r_name, f_fname)
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
        self.reallocate(f_fname, self.room)
        self.assertEqual(1, len(self.room.occupants))
        self.assertEqual(0, len(self.room2.occupants))

    def test_maximum_capacities_of_room_and_office(self):
        living = LivingSpace("Shell")
        office = Office("Camelot")
        self.assertEqual(4, living.capacity)
        self.assertEqual(6, office.capacity)


if __name__ == '__main__':
    unittest.main()
