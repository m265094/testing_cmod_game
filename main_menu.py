# main_menu.py
import pygame
import sys
from button import Button
from game import run_game

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("../testing_cmod_game/assets/sprite/bancroft.JPG")

class StartButton(Button):
    def __init__(self, pos):
        image = pygame.image.load("../testing_cmod_game/assets/sprite/start button.png")  # Replace with your start button image
        font = pygame.font.Font("../testing_cmod_game/assets/font/Debrosee-ALPnL.ttf", 75)  # Replace with your font file
        super().__init__(image, pos, "START", font, "#d7fcd4", "White")

def main_menu():
    running = True

    while running:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font("../testing_cmod_game/assets/font/Debrosee-ALPnL.ttf", 100).render("CMOD GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        START_BUTTON = StartButton(pos=(640, 400))
        QUIT_BUTTON = Button(image=pygame.image.load("../testing_cmod_game/assets/sprite/stop button.png"), pos=(640, 550),
                             text_input="QUIT", font=pygame.font.Font("../testing_cmod_game/assets/font/Debrosee-ALPnL.ttf", 75),
                             base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.check_for_input(MENU_MOUSE_POS):
                    print("Start button clicked!")
                    run_game(screen)
                elif QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    print("Quit button clicked!")
                    running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()