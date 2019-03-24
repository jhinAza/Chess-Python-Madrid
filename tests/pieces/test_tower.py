import unittest

from chess.pieces import Rook
from chess.coordinates import Coordinates


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates('d', 4)
        self.rook = Rook(self.coords, 'white')

    def test_rook_initialization(self):
        self.assertEqual(self.rook.coordinates, self.coords)

    def test_rook_position(self):
        self.assertTupleEqual((3, 3), self.rook.position)

    def test_rook_resource_name(self):
        self.assertEqual('white_rook.png', self.rook.resource_name)

    def test_rook_can_move_ahead(self):
        new_coord = Coordinates('d', 5)
        self.assertTrue(self.rook.can_move_to(new_coord))

    def test_rook_can_move_behind(self):
        new_coord = Coordinates('d', 3)
        self.assertTrue(self.rook.can_move_to(new_coord))

    def test_rook_can_move_to_left(self):
        new_coord = Coordinates('c', 4)
        self.assertTrue(self.rook.can_move_to(new_coord))

    def test_rook_can_move_to_right(self):
        new_coord = Coordinates('e', 4)
        self.assertTrue(self.rook.can_move_to(new_coord))

    def test_rook_can_move_more_than_one_tile(self):
        new_coord = Coordinates('d', 8)
        self.assertTrue(self.rook.can_move_to(new_coord))

    def test_rook_cant_move_diagonally(self):
        new_coord = Coordinates('e', 5)
        self.assertFalse(self.rook.can_move_to(new_coord))
