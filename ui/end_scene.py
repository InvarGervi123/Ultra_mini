# ui/end_scene.py
"""
EndScene – shown when the game ends.

Responsibilities:
- Show final score
- Show high score
- Allow restarting the game or returning to menu

Very simple logic, easy to explain in defense.
"""

import pygame

from interfaces.scene import BaseScene
from ui.widgets import Button
from core.constants import WIDTH, HEIGHT, COLOR_WHITE
from logic.storage import load_highscore, save_highscore


class EndScene(BaseScene):
    """Game over screen."""

    def __init__(self, scene_manager, score: int):
        self.scene_manager = scene_manager
        self.score = score

        # Load and update high score
        self.highscore = load_highscore()
        if self.score > self.highscore:
            self.highscore = self.score
            save_highscore(self.highscore)

        # Fonts
        self.title_font = pygame.font.SysFont(None, 56)
        self.text_font = pygame.font.SysFont(None, 32)
        self.button_font = pygame.font.SysFont(None, 32)

        # Buttons
        self.restart_button = Button(
            pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 20, 240, 50),
            "RESTART",
            self.button_font,
        )

        self.menu_button = Button(
            pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 80, 240, 50),
            "MENU",
            self.button_font,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if self.restart_button.is_clicked(event) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
            from ui.game_scene import GameScene
            self.scene_manager.set_scene(GameScene(self.scene_manager))

        if self.menu_button.is_clicked(event):
            from ui.menu_scene import MenuScene
            self.scene_manager.set_scene(MenuScene(self.scene_manager))

        # Always allow ESC to return to menu
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from ui.menu_scene import MenuScene
            self.scene_manager.set_scene(MenuScene(self.scene_manager))
            return

    def update(self, dt: float) -> None:
        """No logic to update on end screen."""
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Draw end screen UI."""

        # Title
        title_surface = self.title_font.render("GAME OVER", True, COLOR_WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, 120))
        screen.blit(title_surface, title_rect)

        # Score
        score_surface = self.text_font.render(
            f"Your Score: {self.score}", True, COLOR_WHITE
        )
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 180))
        screen.blit(score_surface, score_rect)

        # High score
        highscore_surface = self.text_font.render(
            f"High Score: {self.highscore}", True, COLOR_WHITE
        )
        highscore_rect = highscore_surface.get_rect(center=(WIDTH // 2, 220))
        screen.blit(highscore_surface, highscore_rect)

        # Buttons
        self.restart_button.draw(screen)
        self.menu_button.draw(screen)
