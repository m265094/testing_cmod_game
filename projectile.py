# projectile.py
import pygame
from game_parameters import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill((255, 0, 0))  # Red color, you can customize this
        self.rect = self.image.get_rect(topleft=(x * CELL_SIZE, y * CELL_SIZE))
        self.speed = speed  # Add the speed attribute

    def update(self):
        self.rect.x += self.speed  # Update the projectile's position based on speed
