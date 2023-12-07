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
        self.base_respawn_time = 15000  # Initial respawn time in milliseconds
        self.respawn_time = self.base_respawn_time

    def update_time_until_appear(self, wave):
        # Adjust the respawn time based on the current wave
        self.base_respawn_time -= 1000  # Reduce the base time by 1 second for each wave
        self.base_respawn_time = max(5000, self.base_respawn_time)  # Ensure a minimum time
        self.respawn_time = self.base_respawn_time

    def reset_timer(self):
        self.timer = 0

    def show(self):
        self.visible = True
        self.timer = pygame.time.get_ticks()
        self.update_time_until_appear(wave)  # Update the respawn time based on the current wave

    def hide(self):
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)

    def check_hit(self):
        if self.visible:
            elapsed_time = pygame.time.get_ticks() - self.timer
            return elapsed_time <= 1500
        return False
