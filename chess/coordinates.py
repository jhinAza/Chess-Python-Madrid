from typing import Tuple
from chess import constants

class Coordinates:

    _trap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, letter: str, number: int):
        assert letter in self._trap, 'The letter of a coordinate must be one from a to h'
        assert 1 <= number <= 8, 'The number of a coordinate must be included in [1. 8]'
        self.letter = letter
        self.number = number

    @property
    def matrix_coordinates(self) -> Tuple[int, int]:
        return self.number -1, self._trap.index(self.letter)

    @property
    def color(self):
        coords = self.matrix_coordinates
        return constants.WHITE if all(n % 2 == 0 for n in coords) or all(n % 2 == 1 for n in coords) else constants.BLACK

    def is_before(self, other: 'Coordinates') -> bool:
        return other.letter == self.letter and other.number < self.number

    def is_behind(self, other: 'Coordinates') -> bool:
        return other.letter == self.letter and other.number > self.number

    def distance(self, other: 'Coordinates') -> Tuple[int, int]:
        return self._letter_distance(other), self._number_distance(other)

    def _letter_distance(self, other: 'Coordinates') -> int:
        my_letter = self._trap.index(self.letter)
        other_letter = self._trap.index(other.letter)
        return abs(my_letter - other_letter)

    def _number_distance(self, other: 'Coordinates') -> int:
        return abs(other.number - self.number)

    @classmethod
    def from_matrix_coordinates(cls, coordinates):
        number = coordinates[0] + 1
        letter = cls._trap[coordinates[1]]
        return Coordinates(letter, number)
