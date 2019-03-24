from chess.pieces.base_piece import BasePiece


class Rook(BasePiece):

    min_pieces = 0
    max_pieces = 2

    def can_move_to(self, new_coords):
        position = new_coords.distance(self.coordinates)
        return any(position) and not all(position)
