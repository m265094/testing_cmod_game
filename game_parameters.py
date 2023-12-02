import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60
CELL_SIZE = 40
MAZE_WIDTH = WIDTH // CELL_SIZE
MAZE_HEIGHT = HEIGHT // CELL_SIZE

pygame.init()


# Colors
WHITE = (222, 212, 144)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

PLAYER_POSITION = (3, 3)

# Create Maze
row_0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
row_1 = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0]
row_2 = [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
row_3 = [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,]

maze = [row_0, row_0, row_1, row_1, row_1, row_1, row_2, row_2, row_2, row_1, row_1, row_1, row_1, row_0, row_0]
maze_2 = [row_0, row_2, row_2, row_2, row_3, row_3, row_2, row_2, row_2, row_3, row_3, row_2, row_2, row_2, row_0]

# Pygame setup
clock = pygame.time.Clock()

# Other game constants
lives = 3
wave = 1
score = 0
