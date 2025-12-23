# ui/menu_scene.py
"""
MenuScene – the opening screen of the game.

Responsibilities:
- Show game title
- Show START and QUIT buttons
- Switch scenes when buttons are clicked

NO game logic here.
"""

import pygame

from interfaces.scene import BaseScene
from ui.widgets import Button
from core.constants import WIDTH, HEIGHT, COLOR_WHITE


class MenuScene(BaseScene):
    """Main menu scene."""

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

        # Fonts
        self.title_font = pygame.font.SysFont(None, 64)
        self.button_font = pygame.font.SysFont(None, 36)

        # Buttons
        self.start_button = Button(
            pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 - 30, 240, 50),
            "START GAME",
            self.button_font,
        )

        self.quit_button = Button(
            pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 40, 240, 50),
            "QUIT",
            self.button_font,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if self.start_button.is_clicked(event) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
            from ui.game_scene import GameScene
            self.scene_manager.set_scene(GameScene(self.scene_manager))

        if self.quit_button.is_clicked(event) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Always allow ESC to return to menu
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from ui.menu_scene import MenuScene
            self.scene_manager.set_scene(MenuScene(self.scene_manager))
            return


    def update(self, dt: float) -> None:
        """Menu has no logic to update."""
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Draw menu UI."""
        # Title
        title_surface = self.title_font.render(
            "Math Escape Game", True, COLOR_WHITE
        )
        title_rect = title_surface.get_rect(center=(WIDTH // 2, 120))
        screen.blit(title_surface, title_rect)

        # Buttons
        self.start_button.draw(screen)
        self.quit_button.draw(screen)
