# game.py
import pygame
import sys
import random
from game_parameters import *
from maze import draw_maze
from player import draw_player, move_player
from officer import Officer
from enemy import Enemy
from coin import Coin  # Import the Coin class
INITIAL_PLAYER_LIVES = 3
INITIAL_PLAYER_POSITION = (3, 3)
pygame.mixer.init()
win = pygame.mixer.Sound("../testing_cmod_game/assets/sound/win.wav")
ahem = pygame.mixer.Sound("../testing_cmod_game/assets/sound/ahem_x.wav")
drum = pygame.mixer.Sound("../testing_cmod_game/assets/sound/drum_roll.wav")
chime = pygame.mixer.Sound("../testing_cmod_game/assets/sound/chime.wav")
cannon = pygame.mixer.Sound("../testing_cmod_game/assets/sound/cannon_x.wav")
minus = pygame.mixer.Sound("../testing_cmod_game/assets/sound/peeeooop_x.wav")
game = pygame.mixer.Sound("../testing_cmod_game/assets/sound/mixkit-deep-urban.wav")

def reset_game():
    global player_position, officer, lives, score, wave
    player_position = INITIAL_PLAYER_POSITION
    officer = Officer()
    officer.hide()  # Add this line to hide the officer when resetting the game
    lives = INITIAL_PLAYER_LIVES
    score = 0
    wave = 1

def run_game(screen):
    global player_position, officer, lives, score, wave
    start_time = pygame.time.get_ticks()
    officer = Officer()
    pygame.font.init()
    coins = []
    coin_spawn_interval = 5000  # Time interval for spawning new coins (in milliseconds)
    last_coin_spawn_time = pygame.time.get_ticks()

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

    HEALTH_BAR_WIDTH = 200
    HEALTH_BAR_HEIGHT = 40

    attention_text_font = pygame.font.Font(None, 45)
    attention_text_visible = False  # Initialize attention_text_visible

    enemy_spawn_interval = 15000  # Time interval for spawning a new enemy (in milliseconds)
    last_enemy_spawn_time = pygame.time.get_ticks()

    projectiles = []  # List to store enemy projectiles
    projectile_speed = 5

    while lives > 0 and wave <= 20:
        current_time = pygame.time.get_ticks() - start_time
        clock.tick(FPS)
        required_points = 4 + (wave - 1) * 3

        if score >= required_points:
            wave += 1
            moving_to_wave_text = score_font.render(f"Moving to Wave {wave}", True, (0, 255, 0))
            screen.blit(moving_to_wave_text, (
            WIDTH / 2 - moving_to_wave_text.get_width() / 2, HEIGHT / 2 - moving_to_wave_text.get_height() / 2))
            pygame.display.flip()
            pygame.mixer.Sound.play(cannon)
            pygame.time.delay(2000)  # Display for 2 seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_button.collidepoint(event.pos):
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
                        attention_text_visible = True
                        pygame.mixer.Sound.play(drum)
                        officer.hide()
                    else:
                        lives -= 1
                        attention_text_visible = True
                        pygame.mixer.Sound.play(drum)
                        pygame.mixer.Sound.play(minus)
                    officer.hide()

        if attention_text_visible:
            attention_text = attention_text_font.render("ATTENTION ON DECK!!!", True, (255, 0, 0))
            text_x = WIDTH // 2 - attention_text.get_width() // 2
            text_y = HEIGHT + 20  # Adjust this value to set the vertical position
            screen.blit(attention_text, (text_x, text_y))
            pygame.display.flip()
            pygame.time.delay(2000)  # Display for 2 seconds
            attention_text_visible = False
        screen.fill(WHITE)


        # Check if the officer's time limit has been reached
        if officer.visible:
            elapsed_time = current_time - officer.timer
            if elapsed_time >= 1500:  # 2 seconds
                officer.hide()
                lives -= 1
                pygame.mixer.Sound.play(minus)
                # Display "TOO LATE!" text for 2 seconds
                too_late_text = wave_font.render("TOO LATE!", True, (255, 0, 0))
                screen.blit(too_late_text, (WIDTH // 2 - too_late_text.get_width() // 2, HEIGHT - 50))
                pygame.display.flip()
                pygame.time.delay(2000)
            else:
                text_surface = wave_font.render("A - CALL ATTENTION ON DECK", True, (255, 255, 255))
                screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT - 50))


        draw_maze()


        draw_player(player_position)
        enemy.draw_enemy()
        pygame.draw.rect(screen, GREY, exit_button)  # Draw exit button
        screen.blit(exit_button_text, (exit_button.x + 10, exit_button.y + 10))  # Draw exit button text
        officer.draw(screen)

        # Display wave, score, and lives on the right side of the maze
        wave_text = info_font.render(f"Wave: {wave}", True, (0, 0, 0))
        score_text = info_font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = info_font.render(f"Lives: {lives}", True, (0, 0, 0))

        screen.blit(wave_text, (WIDTH + 10, 10))
        screen.blit(score_text, (WIDTH + 10, 50))
        screen.blit(lives_text, (WIDTH + 10, 90))

        draw_maze()
        for coin in coins:
            coin.draw_coin(screen)
        draw_player(player_position)
        enemy.draw_enemy()

        # Draw health bar with text
        pygame.draw.rect(screen, (255, 0, 0), (10, HEIGHT - 50, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))  # Red background
        pygame.draw.rect(screen, HEALTH_BAR_COLOR,
                         (10, HEIGHT - 50, lives * (HEALTH_BAR_WIDTH / 3), HEALTH_BAR_HEIGHT))  # Dynamic health bar
        health_text = info_font.render("Health Bar", True, (0, 0, 0))
        screen.blit(health_text, (20, HEIGHT - 50))

        pygame.draw.rect(screen, GREY, exit_button)  # Draw exit button
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


        if current_time - last_enemy_spawn_time >= enemy_spawn_interval:
            last_enemy_spawn_time = current_time
            enemy.position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))

            # Shoot 1 projectile
            projectile_direction = (
                player_position[0] - enemy.position[0],
                player_position[1] - enemy.position[1]
            )

            # Normalize the projectile direction
            length = max(abs(projectile_direction[0]), abs(projectile_direction[1]))
            if length != 0:
                projectile_direction = (projectile_direction[0] / length, projectile_direction[1] / length)

            projectiles.append((enemy.position, projectile_direction, projectile_speed))

        if projectiles:
            for proj in projectiles:
                pygame.draw.line(screen, RED, proj[0], (proj[0][0] + proj[1][0], proj[0][1] + proj[1][1]), 2)

        if current_time - last_coin_spawn_time >= coin_spawn_interval:
            last_coin_spawn_time = current_time
            coin_position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
            # Check if the coin position overlaps with existing coins or the enemy, and if it's a white cell
            while any(coin.position == coin_position for coin in coins) or enemy.position == coin_position or \
                    maze[coin_position[1]][coin_position[0]] != 1:
                coin_position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
            coins.append(Coin(position=coin_position, collected=False))

        for coin in coins:
            if not coin.collected and player_position == coin.position:
                coin.collected = True
                score += 1
                pygame.mixer.Sound.play(chime)

        if wave == 1 and len(coins) == 0:
            # Generate 3 coins for wave 1
            for _ in range(3):
                coin_position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
                # Check if the coin position overlaps with existing coins or the enemy, and if it's a white cell
                while any(coin.position == coin_position for coin in coins) or enemy.position == coin_position or \
                        maze[coin_position[1]][coin_position[0]] != 1:
                    coin_position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
                coins.append(Coin(position=coin_position, collected=False))
        elif wave > 1 and len(coins) < wave * 2:
            # Generate 2 additional coins for each wave after wave 1
            for _ in range(2):
                coin_position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
                # Check if the coin position overlaps with existing coins or the enemy, and if it's a white cell
                while any(coin.position == coin_position for coin in coins) or enemy.position == coin_position or \
                        maze[coin_position[1]][coin_position[0]] != 1:
                    coin_position = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
                coins.append(Coin(position=coin_position, collected=False))
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
        screen.fill(GREY)
        message = score_font.render("GAME OVER!!!", True, (255, 0, 0))
        screen.blit(message, (WIDTH / 1.25 - message.get_width() / 2, HEIGHT / 1.5 - message.get_height() / 2))
        score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text,
                    (WIDTH / 1.25 - score_text.get_width() / 2, HEIGHT / 1.5 - 3 * score_text.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(3000)

    return current_time
