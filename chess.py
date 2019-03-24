from collections import deque

import pygame
from pygame.locals import *
import yaml

from chess import pieces, coordinates, table, constants
from chess.coordinates import Coordinates


class Game:

    def __init__(self):
        self._state = self._load_state()
        self.table = table.Table(state=self._state)
        self.running = False
        self._selected = False
        pygame.init()
        pygame.font.init()
        self._init_screen()
        pygame.display.set_caption('Chess')

    def run(self):
        clock = pygame.time.Clock()
        self.running = True

        times = deque(maxlen=30)
        try:
            while self.running:
                dt = clock.tick(30) / 1000.
                times.append(clock.get_fps())
                self._handle_input()
                self._draw()
                pygame.display.update()
        except KeyboardInterrupt:
            self.running = False

    def _load_state(self):
        return yaml.load(open('state.yaml', 'r'))

    def _draw(self):
        for row in self.table.iter_rows():
            for coords, piece in row:
                position = coords.matrix_coordinates
                position = position[1], position[0]
                start = [x * 100 for x in position]
                end = (100, 100)
                rect = pygame.Rect(*start, *end)
                if self._selected == position:
                    pygame.draw.rect(self.screen, pygame.Color('gold'), rect)
                    selected_start = [x + 10 for x in start]
                    selected_end = [x - 20 for x in end]
                    pygame.draw.rect(self.screen, pygame.Color(coords.color), Rect(*selected_start, *selected_end))
                else:
                    pygame.draw.rect(self.screen, pygame.Color(coords.color), rect)
                if piece:
                    image = self._get_asset(piece)
                    image_start = [x + 15 for x in start]
                    self.screen.blit(image, image_start)

    def _handle_input(self):
        poll = pygame.event.poll

        event = poll()
        while event:
            if event.type == QUIT:
                self.running = False
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    break
            elif event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                column = position[0] // 100
                row = position[1] // 100
                coords = Coordinates.from_matrix_coordinates((row, column))
                piece = self.table.get(coords)
                if piece and piece.color == 'white':
                    self._selected = (column, row)
                elif self._selected:
                    selected_coords = Coordinates.from_matrix_coordinates((self._selected[1], self._selected[0]))
                    piece = self.table.get(selected_coords)
                    if piece.can_move_to(coords):
                        self.table.move_piece(selected_coords, coords)
                    self._selected = None
                else:
                    self._selected = None

            event = poll()

    def _init_screen(self):
        self.screen = pygame.display.set_mode((800, 800))

    def _get_asset(self, piece: pieces.BasePiece) -> pygame.image:
        asset = f"assets/{piece.resource_name}"
        image = pygame.image.load(asset)
        return pygame.transform.scale(image, (70,70))


if __name__ == '__main__':
    game = Game()
    game.run()
