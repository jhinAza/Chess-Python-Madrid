from chess.pieces.base_piece import BasePiece


class Pawn(BasePiece):

    min_pieces = 0
    max_pieces = 8

    def can_move_to(self, new_coords):
        if self.color == 'white' and new_coords.is_behind(self.coordinates):
            return new_coords.distance(self.coordinates) == (0, 1)
        elif self.color == 'black' and new_coords.is_before(self.coordinates):
            return new_coords.distance(self.coordinates) == (0, 1)
        return False
