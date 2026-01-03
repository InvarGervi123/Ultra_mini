# ui/sprites.py
"""
Simple sprite classes for the game.

- Player: visual representation of the player (blinks on FLASH_EVENT)
- QuestionSprite: renders the current question as a sprite (keeps image/rect)

Both inherit from pygame.sprite.Sprite so they work with Groups.
"""

import pygame
from core.constants import COLOR_PLAYER, COLOR_WHITE


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.size = (48, 48)
        self.base_color = COLOR_PLAYER
        self.flash_color = (255, 255, 255)
        self.flashing = False

        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self._render()

    def _render(self) -> None:
        color = self.flash_color if self.flashing else self.base_color
        self.image.fill(color)

    def toggle_flash(self) -> None:
        self.flashing = not self.flashing
        self._render()

    def update(self, *args) -> None:
        # Nothing dynamic for now; state changes via toggle_flash
        pass


class QuestionSprite(pygame.sprite.Sprite):
    def __init__(self, text: str, font: pygame.font.Font, pos: tuple[int, int]):
        super().__init__()
        self.font = font
        self.text = text
        self.color = COLOR_WHITE

        # initial render
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=pos)

    def set_text(self, text: str) -> None:
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, *args) -> None:
        # Question changes are applied explicitly via set_text
        pass
