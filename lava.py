# coin.py
import pygame
from game_parameters import LAVA_COLOR, CELL_SIZE

class Lava:
    def __init__(self, position, collected=False):
        self.position = position
        self.collected = collected

    def draw_lava(self, screen):
        if not self.collected:
            pygame.draw.rect(screen, LAVA_COLOR,
                             (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
