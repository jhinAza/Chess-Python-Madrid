from chess.pieces.base_piece import BasePiece
from chess.coordinates import Coordinates

class King(BasePiece):

    min_pieces = 1
    max_pieces = 1

    def can_move_to(self, new_coords: Coordinates):
        distance = new_coords.distance(self.coordinates)
        return any(d == 1 for d in distance) and all(d <= 1 for d in distance)
