import unittest

from chess.pieces.pawn import Pawn
from chess.coordinates import Coordinates

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates('d', 4)
        self.pawn = Pawn(self.coords, 'white')

    def test_pawn_initialization(self):
        self.assertEqual(self.pawn.coordinates, self.coords)

    def test_pawn_position(self):
        self.assertTupleEqual((3, 3), self.pawn.position)

    def test_pawn_resource_name(self):
        self.assertEqual('white_pawn.png', self.pawn.resource_name)

    def test_pawn_can_move_ahead(self):
        new_coord = Coordinates('d', 5)
        self.assertTrue(self.pawn.can_move_to(new_coord))

    def test_pawn_cant_move_behind(self):
        new_coord = Coordinates('d', 3)
        self.assertFalse(self.pawn.can_move_to(new_coord))

    def test_cant_move_more_than_one_tile(self):
        new_coord = Coordinates('d', 8)
        self.assertFalse(self.pawn.can_move_to(new_coord))

    def test_pawn_cant_move_at_the_sides(self):
        new_coord = Coordinates('c', 4)
        self.assertFalse(self.pawn.can_move_to(new_coord))
        new_coord = Coordinates('e', 4)
        self.assertFalse(self.pawn.can_move_to(new_coord))
