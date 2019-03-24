from typing import List

from chess.pieces import Pawn, King, Knight, Queen, Bishop, Rook
from chess.pieces.base_piece import BasePiece
from chess.coordinates import Coordinates


class Table:

    _piece_map = {
        'pawn': Pawn,
        'king': King,
        'queen': Queen,
        'rook': Rook,
        'knight': Knight,
        'bishop': Bishop,
    }

    def __init__(self, state: dict = None):
        self.matrix: List[List[BasePiece]] = [[None for _ in range(8)] for _ in range(8)]
        if not state:
            state = dict()
        self.state = state
        self._fill_state()

    def move_piece(self, from_position: Coordinates, to_position: Coordinates) -> bool:
        from_matrix = from_position.matrix_coordinates
        piece = self.matrix[from_matrix[0]][from_matrix[1]]
        if piece and piece.can_move_to(to_position):
            piece.coordinates = to_position
            to_matrix = to_position.matrix_coordinates
            self.matrix[to_matrix[0]][to_matrix[1]] = piece
            self.matrix[from_matrix[0]][from_matrix[1]] = None
            return True
        return False

    def get(self, position: Coordinates) -> BasePiece:
        coords = position.matrix_coordinates
        return self.matrix[coords[0]][coords[1]]

    def _fill_state(self):
        for color, pieces in self.state.items():
            self._set_pieces(pieces, color)

    def _set_pieces(self, pieces: dict, color:str):
        for piece_type, coords in pieces.items():
            Piece = self._piece_map.get(piece_type)
            if Piece.min_pieces <= len(coords) <= Piece.max_pieces:
                for piece_coord in coords:
                    letter = piece_coord[0]
                    number = int(piece_coord[1])
                    coord = Coordinates(letter, number)
                    matrix_coordinates = coord.matrix_coordinates
                    self.matrix[matrix_coordinates[0]][matrix_coordinates[1]] = Piece(coord, color)

    def iter_rows(self):
        for row_number, row in enumerate(self.matrix):
            yield _RowIterator(row, row_number)


class _RowIterator:
    def __init__(self, row, row_number):
        self._row_number = row_number
        self._row = row
        self._next = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= 8:
            raise StopIteration()
        piece = self._row[self._next]
        coord = Coordinates.from_matrix_coordinates((self._row_number, self._next))
        self._next += 1
        return coord, piece

