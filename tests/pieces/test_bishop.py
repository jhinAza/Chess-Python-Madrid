import unittest

from chess.pieces import Bishop
from chess.coordinates import Coordinates


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates('d', 4)
        self.bishop = Bishop(self.coords, 'white')

    def test_bishop_initialization(self):
        self.assertEqual(self.bishop.coordinates, self.coords)

    def test_bishop_position(self):
        self.assertTupleEqual((3, 3), self.bishop.position)

    def test_bishop_resource_name(self):
        self.assertEqual('white_bishop.png', self.bishop.resource_name)

    def test_bishop_cant_move_ahead(self):
        new_coord = Coordinates('d', 5)
        self.assertFalse(self.bishop.can_move_to(new_coord))

    def test_bishop_cant_move_behind(self):
        new_coord = Coordinates('d', 3)
        self.assertFalse(self.bishop.can_move_to(new_coord))

    def test_bishop_cant_move_to_the_left(self):
        new_coord = Coordinates('c', 4)
        self.assertFalse(self.bishop.can_move_to(new_coord))

    def test_bishop_cant_move_to_the_right(self):
        new_coord = Coordinates('e', 4)
        self.assertFalse(self.bishop.can_move_to(new_coord))

    def test_bishop_can_move_diagonally(self):
        new_coord = Coordinates('e', 5)
        self.assertTrue(self.bishop.can_move_to(new_coord))
