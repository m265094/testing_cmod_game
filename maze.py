import pygame
import sys
from game_parameters import *

def draw_maze():
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if maze[row][col] == 1:
                color = WHITE
            else:
                color = BLACK
            #color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_maze_2():
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if maze_2[row][col] == 1:
                color = WHITE
            else:
                color = BLACK
            #color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
