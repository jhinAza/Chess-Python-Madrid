from chess.pieces.base_piece import BasePiece


class Bishop(BasePiece):

    min_pieces = 0
    max_pieces = 2

    def can_move_to(self, new_coords):
        distance = new_coords.distance(self.coordinates)
        return all(distance) and distance[0] == distance[1]
