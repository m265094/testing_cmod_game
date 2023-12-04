# officer.py
import pygame
import random
from game_parameters import *

class Officer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../testing_cmod_game/assets/sprite/officer.JPG").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (20 * CELL_SIZE, 6 * CELL_SIZE)
        self.visible = False
        self.timer = 0
        self.time_until_appear = random.randint(15, 20) * 1000  # Initial random time in milliseconds

    def update_time_until_appear(self, wave):
        # Adjust the time until appear based on the current wave
        self.time_until_appear = max(5000, 20000 - (wave - 1) * 1000)

    def show(self):
        self.visible = True
        self.timer = pygame.time.get_ticks()

    def hide(self):
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)

    def check_hit(self):
        if self.visible:
            elapsed_time = pygame.time.get_ticks() - self.timer
            if elapsed_time <= 6000:  # 6 seconds
                return True
            else:
                return False
