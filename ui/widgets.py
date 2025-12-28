# ui/widgets.py
"""
UI widgets used by scenes.

Contains:
- Button   : clickable rectangle with text
- InputBox : simple numeric text input

These widgets are intentionally VERY simple and readable.
No animations, no sounds, no tricks.
"""

import pygame
from core.constants import COLOR_BUTTON, COLOR_BUTTON_BORDER, COLOR_WHITE


class Button:
    """
    Simple clickable button.

    Used in MenuScene and EndScene.
    """

    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font):
        self.rect = rect
        self.text = text
        self.font = font

    def is_clicked(self, event: pygame.event.Event) -> bool:
        """
        Check if the button was clicked.

        Returns True only when:
        - mouse button is pressed
        - cursor is inside the button rectangle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the button."""
        pygame.draw.rect(screen, COLOR_BUTTON, self.rect, border_radius=8)
        pygame.draw.rect(
            screen, COLOR_BUTTON_BORDER, self.rect, width=2, border_radius=8
        )

        text_surface = self.font.render(self.text, True, COLOR_WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class InputBox:
    """
    Very simple numeric input box.

    Rules:
    - Accepts digits only
    - Backspace deletes
    - Enter submits (handled by the scene)
    """

    def __init__(self, rect: pygame.Rect, font: pygame.font.Font):
        self.rect = rect
        self.font = font
        self.text: str = ""

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle keyboard input."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit() and len(self.text) < 13:
                self.text += event.unicode

    def clear(self) -> None:
        """Clear the input box."""
        self.text = ""

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the input box and current text."""
        pygame.draw.rect(screen, COLOR_BUTTON, self.rect, border_radius=6)
        pygame.draw.rect(
            screen, COLOR_BUTTON_BORDER, self.rect, width=2, border_radius=6
        )

        text_surface = self.font.render(self.text, True, COLOR_WHITE)
        text_rect = text_surface.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
        screen.blit(text_surface, text_rect)
