from chess.pieces.base_piece import BasePiece


class Knight(BasePiece):

    min_pieces = 0
    max_pieces = 2

    def can_move_to(self, new_coords):
        position = new_coords.distance(self.coordinates)
        return max(position) == 2 and min(position) == 1
