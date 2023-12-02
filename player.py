#player.py
import pygame
import sys
from game_parameters import *

def draw_player(player_pos):
        pygame.draw.rect(screen, RED, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_player(player_pos, direction):
    new_pos = player_pos
    print(player_pos)
    if direction == "UP" and player_pos[1] > 0 and maze[player_pos[1] - 1][player_pos[0]] == 1:
        new_pos = (player_pos[0], player_pos[1] - 1)
    elif direction == "DOWN" and player_pos[1] < MAZE_HEIGHT - 1 and maze[player_pos[1] + 1][player_pos[0]] == 1:
        new_pos = (player_pos[0], player_pos[1] + 1)
    elif direction == "LEFT" and player_pos[0] > 0 and maze[player_pos[1]][player_pos[0] - 1] == 1:
        new_pos = (player_pos[0] - 1, player_pos[1])
    elif direction == "RIGHT" and player_pos[0] < MAZE_WIDTH - 1 and maze[player_pos[1]][player_pos[0] + 1] == 1:
        new_pos = (player_pos[0] + 1, player_pos[1])

    return new_pos
