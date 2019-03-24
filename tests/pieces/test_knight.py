import unittest

from chess.pieces import Knight
from chess.coordinates import Coordinates

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates('d', 4)
        self.knight = Knight(self.coords, 'white')

    def test_knight_initialization(self):
        self.assertEqual(self.knight.coordinates, self.coords)

    def test_knight_position(self):
        self.assertTupleEqual((3, 3), self.knight.position)

    def test_knight_resource_name(self):
        self.assertEqual('white_knight.png', self.knight.resource_name)

    def test_knight_cant_move_ahead(self):
        new_coord = Coordinates('d', 5)
        self.assertFalse(self.knight.can_move_to(new_coord))

    def test_knight_cant_move_behind(self):
        new_coord = Coordinates('d', 3)
        self.assertFalse(self.knight.can_move_to(new_coord))

    def test_knight_cant_move_to_the_left(self):
        new_coord = Coordinates('c', 4)
        self.assertFalse(self.knight.can_move_to(new_coord))

    def test_knight_cant_move_to_the_right(self):
        new_coord = Coordinates('e', 4)
        self.assertFalse(self.knight.can_move_to(new_coord))

    def test_knight_cant_move_diagonally(self):
        new_coord = Coordinates('e', 5)
        self.assertFalse(self.knight.can_move_to(new_coord))

    def test_knight_can_move_on_l(self):
        new_coord = Coordinates('e', 7)
        self.assertTrue(self.knight.can_move_to(new_coord))
