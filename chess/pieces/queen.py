from chess.pieces.base_piece import BasePiece
from chess.coordinates import Coordinates


class Queen(BasePiece):

    min_pieces = 0
    max_pieces = 1

    def can_move_to(self, new_coords: Coordinates):
        distance = new_coords.distance(self.coordinates)
        if any(distance):
            if distance[0] and not distance[1]:
                return True
            elif not distance[0] and distance[1]:
                return True
            elif distance[0] == distance[1]:
                return True
        return False
