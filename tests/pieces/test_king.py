import unittest

from chess.pieces import King
from chess.coordinates import Coordinates


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates('d', 4)
        self.king = King(self.coords, 'white')

    def test_king_initialization(self):
        self.assertEqual(self.king.coordinates, self.coords)

    def test_king_position(self):
        self.assertTupleEqual((3, 3), self.king.position)

    def test_king_resource_name(self):
        self.assertEqual('white_king.png', self.king.resource_name)

    def test_king_can_move_ahead(self):
        new_coord = Coordinates('d', 5)
        self.assertTrue(self.king.can_move_to(new_coord))

    def test_king_can_move_behind(self):
        new_coord = Coordinates('d', 3)
        self.assertTrue(self.king.can_move_to(new_coord))

    def test_king_cant_move_more_than_one_tile(self):
        new_coord = Coordinates('d', 8)
        self.assertFalse(self.king.can_move_to(new_coord))

    def test_king_can_move_to_left(self):
        new_coord = Coordinates('c', 4)
        self.assertTrue(self.king.can_move_to(new_coord))

    def test_king_can_move_to_right(self):
        new_coord = Coordinates('e', 4)
        self.assertTrue(self.king.can_move_to(new_coord))
