#enemy.py
import pygame
import sys
import random
from game_parameters import *

enemy_possible_positions = [
    (4, 3),
    (10, 3),
    (16, 3),
    (4, 11),
    (10, 11),
    (16, 11),
]


class Enemy:
    def __init__(self):
        self.position = random.choice(enemy_possible_positions)
        self.projectiles = []

    def draw_enemy(self):
        pygame.draw.rect(screen, GREEN,
                         (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for projectile in self.projectiles:
            projectile.draw()

    def shoot_projectile(self, player_position):
        # Start the projectile at the enemy's position
        start_pos = (self.position[0] * CELL_SIZE + CELL_SIZE // 2, self.position[1] * CELL_SIZE + CELL_SIZE // 2)

        # Target the player's position
        target = (player_position[0] * CELL_SIZE + CELL_SIZE // 2, player_position[1] * CELL_SIZE + CELL_SIZE // 2)

        # Create a new projectile with the updated start and target positions
        projectile = Projectile(start_pos, target)
        self.projectiles.append(projectile)

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.update()


class Projectile:
    def __init__(self, start_pos, target_pos):
        self.position = [start_pos[0] * CELL_SIZE + CELL_SIZE // 2, start_pos[1] * CELL_SIZE + CELL_SIZE // 2]
        self.target = [target_pos[0] * CELL_SIZE + CELL_SIZE // 2, target_pos[1] * CELL_SIZE + CELL_SIZE // 2]
        self.speed = 5

    def update(self):
        direction = pygame.math.Vector2(self.target[0] - self.position[0], self.target[1] - self.position[1])
        direction.normalize_ip()
        self.position[0] += direction.x * self.speed
        self.position[1] += direction.y * self.speed

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.position[0]), int(self.position[1])), 5)


def pick_random_enemy_position():
    return random.choice(enemy_possible_positions)