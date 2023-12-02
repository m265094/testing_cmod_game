# projectile.py
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Red color for the projectile
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # Add movement logic here if needed
        pass
