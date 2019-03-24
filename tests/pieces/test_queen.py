import unittest

from chess.pieces import Queen
from chess.coordinates import Coordinates


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates('d', 4)
        self.queen = Queen(self.coords, 'white')

    def test_queen_initialization(self):
        self.assertEqual(self.queen.coordinates, self.coords)

    def test_queen_position(self):
        self.assertTupleEqual((3, 3), self.queen.position)

    def test_queen_resource_name(self):
        self.assertEqual('white_queen.png', self.queen.resource_name)

    def test_queen_can_move_ahead(self):
        new_coord = Coordinates('d', 5)
        self.assertTrue(self.queen.can_move_to(new_coord))

    def test_queen_can_move_behind(self):
        new_coord = Coordinates('d', 3)
        self.assertTrue(self.queen.can_move_to(new_coord))

    def test_queen_can_move_to_left(self):
        new_coord = Coordinates('c', 4)
        self.assertTrue(self.queen.can_move_to(new_coord))

    def test_queen_can_move_to_right(self):
        new_coord = Coordinates('e', 4)
        self.assertTrue(self.queen.can_move_to(new_coord))

    def test_queen_can_move_more_than_one_tile(self):
        new_coord = Coordinates('d', 8)
        self.assertTrue(self.queen.can_move_to(new_coord))

    def test_queen_can_move_diagonally(self):
        new_coord = Coordinates('e', 5)
        self.assertTrue(self.queen.can_move_to(new_coord))
