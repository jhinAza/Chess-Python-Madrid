import unittest

from chess.coordinates import Coordinates
from chess import constants


class TestCoordinates(unittest.TestCase):

    def setUp(self):
        self.coordinates = Coordinates('d', 4)

    def test_coordinates_initialization(self):
        self.assertEqual('d', self.coordinates.letter)
        self.assertEqual(4, self.coordinates.number)

    def test_coordinates_matrix_coordinates(self):
        self.assertEqual((3, 3), self.coordinates.matrix_coordinates)

    def test_is_before(self):
        new_coord = Coordinates('d', 5)
        self.assertTrue(new_coord.is_before(self.coordinates))
        self.assertFalse(self.coordinates.is_before(new_coord))

    def test_is_behind(self):
        new_coord = Coordinates('d', 5)
        self.assertFalse(new_coord.is_behind(self.coordinates))
        self.assertTrue(self.coordinates.is_behind(new_coord))

    def test_distance(self):
        new_coord = Coordinates('d', 4)
        self.assertEqual((0, 0), self.coordinates.distance(new_coord))
        new_coord = Coordinates('d', 5)
        self.assertEqual((0, 1), self.coordinates.distance(new_coord))
        new_coord = Coordinates('e', 4)
        self.assertEqual((1, 0), self.coordinates.distance(new_coord))
        new_coord = Coordinates('e', 5)
        self.assertEqual((1, 1), self.coordinates.distance(new_coord))
        new_coord = Coordinates('d', 3)
        self.assertEqual((0, 1), self.coordinates.distance(new_coord))
        new_coord = Coordinates('c', 4)
        self.assertEqual((1, 0), self.coordinates.distance(new_coord))
        new_coord = Coordinates('c', 3)
        self.assertEqual((1, 1), self.coordinates.distance(new_coord))

    def test_color(self):
        coord = Coordinates('a', 1)
        self.assertEqual(constants.BLACK, coord.color)
        coord = Coordinates('b', 2)
        self.assertEqual(constants.BLACK, coord.color)
        coord = Coordinates('a', 2)
        self.assertEqual(constants.WHITE, coord.color)
        coord = Coordinates('b', 1)
        self.assertEqual(constants.WHITE, coord.color)
