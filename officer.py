# game.py
from game_parameters import *
import pygame
import sys
import random
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

class Officer:
    def __init__(self):
        self.position = (16, 16)
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

    def draw(self):
        if self.visible:
            pygame.draw.rect(screen, BLUE, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_officer(self):
        self.draw()

    def check_hit(self):
        if self.visible:
            elapsed_time = pygame.time.get_ticks() - self.timer
            if elapsed_time <= 6000:  # 6 seconds
                return True
            else:
                return False

# Officer setup
officer = Officer()

# Main game loop
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Officer logic
    officer.update_time_until_appear(wave)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if officer.check_hit():
            # Increase score
            score += 1
        else:
            # Decrease lives
            lives -= 1

        # Hide the officer after checking
        officer.hide()

    # Check if it's time for the officer to appear
    if pygame.time.get_ticks() >= officer.time_until_appear:
        officer.show()

    # Draw everything
    screen.fill(WHITE)
    officer.draw_officer()
    officer.draw()

    # Update the display
    pygame.display.flip()
