from abc import ABCMeta, abstractmethod
from chess.coordinates import Coordinates


class BasePiece(metaclass=ABCMeta):

    min_pieces = 1
    max_pieces = 1

    def __init__(self, coordinates: Coordinates, color: str):
        self.coordinates = coordinates
        self.color = color

    @property
    def position(self):
        return self.coordinates.matrix_coordinates

    @property
    def resource_name(self) -> str:
        return "{color}_{piece}.png".format(piece=self.__class__.__name__.lower(), color=self.color)

    @abstractmethod
    def can_move_to(self, coords: Coordinates):
        pass
