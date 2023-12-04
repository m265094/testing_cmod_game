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
        self.base_time_until_appear = random.randint(15, 20) * 1000  # Initial random time in milliseconds
        self.time_until_appear = self.base_time_until_appear

    def update_time_until_appear(self, wave):
        # Adjust the time until appear based on the current wave
        self.base_time_until_appear -= 2000  # Reduce the base time by 2 seconds for each wave
        self.base_time_until_appear = max(10000, self.base_time_until_appear)  # Ensure a minimum time
        self.time_until_appear = self.base_time_until_appear

    def reset_timer(self):
        self.timer = 0
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
            if elapsed_time <= 1500:
                return True
            else:
                return False
