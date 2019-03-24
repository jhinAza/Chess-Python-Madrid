import unittest

from chess.table import Table
from chess.pieces import Pawn
from chess.coordinates import Coordinates


class TestTable(unittest.TestCase):

    state = {
        'black': {
            'pawn': ['a2', 'b2', 'c2']
        }
    }

    def setUp(self):
        self.table = Table(self.state)

    def test_initialization(self):
        table = Table()
        self.assertFalse(table.state)
        for row in table.matrix:
            for piece in row:
                self.assertIsNone(piece)

    def test_get(self):
        piece = self.table.get(Coordinates('b', 2))
        self.assertIsInstance(piece, Pawn)
        piece = self.table.get(Coordinates('a', 1))
        self.assertIsNone(piece)

    def test_move_piece(self):
        old = Coordinates('b', 2)
        new = Coordinates('b', 3)
        move = self.table.move_piece(old, new)
        self.assertTrue(move)
        self.assertIsInstance(self.table.get(new), Pawn)
        self.assertIsNone(self.table.get(old))
