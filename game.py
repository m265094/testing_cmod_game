# game.py
import pygame
import sys
import random
from game_parameters import *
from maze import draw_maze
from player import draw_player, move_player
from officer import Officer
from enemy import Enemy



def run_game(screen):
    print("Running the game!")
    global player_lives, current_wave, projectiles, player_position, officer, lives, score, wave
    officer = Officer()
    pygame.font.init()

    # Load fonts
    score_font = pygame.font.Font("../testing_cmod_game/assets/font/Branda-yolq.ttf", 40)
    info_font = pygame.font.Font("../testing_cmod_game/assets/font/Branda-yolq.ttf", 30)
    wave_font = pygame.font.Font(None, 36)  # Define wave font

    officer_disappeared = False  # Flag to track officer disappearance
    enemy = Enemy()
    clock = pygame.time.Clock()

    # Define the time range for officer appearance (in milliseconds)
    officer_appearance_start_time = 15000  # 15 seconds
    officer_appearance_end_time = 20000    # 20 seconds

    # Flag to track whether officer has appeared in the current wave
    officer_appeared = False

    exit_button = pygame.Rect(10, 10, 100, 50)  # Define exit button position and size
    exit_button_text = pygame.font.Font(None, 36).render("Exit", True, BLACK)

    while lives > 0 and wave <= 20:
        current_time = pygame.time.get_ticks()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_position = move_player(player_position, "UP")
                elif event.key == pygame.K_DOWN:
                    player_position = move_player(player_position, "DOWN")
                elif event.key == pygame.K_LEFT:
                    player_position = move_player(player_position, "LEFT")
                elif event.key == pygame.K_RIGHT:
                    player_position = move_player(player_position, "RIGHT")
                elif event.key == pygame.K_a:
                    if officer.check_hit():
                        score += 1
                    else:
                        lives -= 1
                    officer.hide()
            if officer.visible:
                text_surface = wave_font.render("A - CALL ATTENTION ON DECK", True, (255, 255, 255))
                screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT - 50))
            elif officer_appeared and not officer.visible:
                # Officer has disappeared, hide the text
                text_surface = wave_font.render("", True, (255, 255, 255))


            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw everything
        screen.fill(WHITE)
        draw_maze()
        draw_player(player_position)
        enemy.draw_enemy()
        pygame.draw.rect(screen, RED, exit_button)  # Draw exit button
        screen.blit(exit_button_text, (exit_button.x + 10, exit_button.y + 10))  # Draw exit button text
        officer.draw(screen)

        # Display wave, score, and lives on the right side of the maze
        wave_text = info_font.render(f"Wave: {wave}", True, (0, 0, 0))
        score_text = info_font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = info_font.render(f"Lives: {lives}", True, (0, 0, 0))

        screen.blit(wave_text, (WIDTH + 10, 10))
        screen.blit(score_text, (WIDTH + 10, 50))
        screen.blit(lives_text, (WIDTH + 10, 90))

        if officer.visible:
            text_surface = wave_font.render("A - CALL ATTENTION ON DECK", True, (255, 255, 255))
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT - 50))

        pygame.display.flip()

        if wave == 1:
            enemy.draw_enemy()
            if not officer_appeared and 5000 < current_time < 10000:  # Officer appears between 5 and 10 seconds
                officer.show()
                officer_appeared = True
        elif wave <= 20:
            num_enemies = min(wave, 5)
            for _ in range(num_enemies):
                enemy.draw_enemy()

            if not officer_appeared and officer_appearance_start_time < current_time < officer_appearance_end_time:
                officer.show()
                officer_appeared = True

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
