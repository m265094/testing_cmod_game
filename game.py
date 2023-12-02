# game.py
import pygame
import sys
import random
from enemy import Enemy
from game_parameters import *
from maze import draw_maze, draw_maze_2
from player import draw_player
from officer import Officer

def run_game(screen):  # Add 'screen' as a parameter
    print("Running the game!")
    global player_lives, current_wave, projectiles, player_position, officer, lives, score, wave
    # Your existing game setup code

    # Initialize the Pygame font module
    pygame.font.init()

    # Load fonts
    score_font = pygame.font.Font("../testing_cmod_game/assets/font/Branda-yolq.ttf", 80)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Game")
    enemy = Enemy()  # Create an instance of the Enemy class
    clock = pygame.time.Clock()

    while lives > 0 and wave <= 20:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if officer.check_hit():
                        score += 1
                    else:
                        lives -= 1

                    officer.hide()

        # Your existing game logic code

        pygame.display.flip()

        screen.fill(WHITE)
        draw_maze()
        draw_player(player_position)
        Enemy.draw_enemy()
        Officer.draw_officer()
        Officer.draw()
        pygame.display.flip()

        if wave == 1:
            enemy.draw_enemy()  # Change this line
            if random.randint(1, 100) < 5:
                officer.show()

        elif wave <= 20:
            num_enemies = min(wave, 5)
            for _ in range(num_enemies):
                enemy.draw_enemy()  # Change this line

            num_officers = min(wave, 5)
            for _ in range(num_officers):
                if random.randint(1, 100) < wave * 5:
                    officer.show()

        if score >= wave * 5:
            wave += 1

        # Add print statements for debugging
        print(f"Wave: {wave}, Score: {score}, Lives: {lives}")

    if wave > 20:
        win_message = score_font.render("YOU WIN!!!", True, (0, 255, 0))
        screen.blit(win_message, (WIDTH / 2 - win_message.get_width() / 2, HEIGHT / 2 - win_message.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(3000)

    else:
        message = score_font.render("GAME OVER!!!", True, (255, 0, 0))
        screen.blit(message, (WIDTH / 2 - message.get_width() / 2, HEIGHT / 2 - message.get_height() / 2))
        score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text,
                    (WIDTH / 2 - score_text.get_width() / 2, HEIGHT / 2 - 3 * score_text.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(3000)



