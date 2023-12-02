import pygame
import sys
class Button:
    def __init__(self, pos, text_input, font, base_color, hovering_color, image=None):
        self.image = image or self._render_text(text_input, font, base_color)
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def _render_text(self, text_input, font, color):
        return font.render(text_input, True, color)

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)

    def change_color(self, position):
        if self.check_for_input(position):
            self.image = self._render_text(self.text_input, self.font, self.hovering_color)
        else:
            self.image = self._render_text(self.text_input, self.font, self.base_color)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
