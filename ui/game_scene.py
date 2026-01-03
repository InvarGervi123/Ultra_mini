# ui/game_scene.py
"""
GameScene – the main gameplay screen.

This scene is responsible for:
- Showing a math question
- Reading user input
- Handling a countdown timer
- Increasing difficulty (less time each level)
- Switching to EndScene when time is up

This file is the MOST IMPORTANT one for your defense,
so everything here is written in the simplest possible way.
"""

import pygame

from interfaces.scene import BaseScene
from logic.questions import MixedQuestion
from logic.difficulty import next_time_limit
from core.constants import (
    WIDTH,
    HEIGHT,
    START_TIME_LIMIT,
    COLOR_WHITE,
    COLOR_WARNING,
)
from core.events import TICK_EVENT, TIME_UP_EVENT, FLASH_EVENT
from ui.sprites import Player, QuestionSprite
from ui.widgets import InputBox
from ui.end_scene import EndScene



class GameScene(BaseScene):
    """Main game scene: timed math questions."""

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

        # Fonts
        self.question_font = pygame.font.SysFont(None, 48)
        self.info_font = pygame.font.SysFont(None, 28)

        # Game state
        self.level: int = 1
        self.score: int = 0

        # Time handling
        self.time_limit: float = START_TIME_LIMIT
        self.time_left: float = self.time_limit

        # Current question
        self.question = MixedQuestion()

        # Input box for answer
        self.input_box = InputBox(
            pygame.Rect(WIDTH // 2 - 80, HEIGHT // 2 + 40, 160, 40),
            self.info_font,
        )

        # Sprites: player and question rendered as sprites
        self.sprites = pygame.sprite.Group()
        # Player on the left side
        self.player_sprite = Player((80, HEIGHT // 2))
        self.sprites.add(self.player_sprite)

        # Question rendered as a sprite (centered above input)
        self.question_sprite = QuestionSprite(self.question.text, self.question_font, (WIDTH // 2, HEIGHT // 2 - 40))
        self.sprites.add(self.question_sprite)

    # --------------------------------------------------
    # Event handling
    # --------------------------------------------------
    def handle_event(self, event: pygame.event.Event) -> None:
        """
        Handle:
        - keyboard input
        - custom timer events
        """

        # Always allow ESC to return to menu
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from ui.menu_scene import MenuScene
            self.scene_manager.set_scene(MenuScene(self.scene_manager))
            return

        # Handle text input
        self.input_box.handle_event(event)

        # When ENTER is pressed -> submit answer
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.check_answer()

        # Custom event: timer tick
        if event.type == TICK_EVENT:
            self.time_left -= 0.1

            if self.time_left <= 0:
                pygame.event.post(pygame.event.Event(TIME_UP_EVENT))

        # Custom event: flash (toggle player blink)
        if event.type == FLASH_EVENT:
            self.player_sprite.toggle_flash()

        # Custom event: time is up
        if event.type == TIME_UP_EVENT:
            self.scene_manager.set_scene(EndScene(self.scene_manager, self.score))

    # --------------------------------------------------
    # Game logic
    # --------------------------------------------------
    def update(self, dt: float) -> None:
        """
        Game logic update.

        dt is not strictly needed here because
        we use TICK_EVENT for timing,
        but it is kept for consistency.
        """
        # update sprites (if they have animations / state)
        self.sprites.update(dt)

    def check_answer(self) -> None:
        """Check user answer and move to next level if correct."""
        if self.question.is_correct(self.input_box.text):
            self.score += 1
            self.level += 1

            # Make next level faster
            self.time_limit = next_time_limit(self.time_limit)
            self.time_left = self.time_limit

            # New question
            self.question = MixedQuestion()
            # update question sprite text
            self.question_sprite.set_text(self.question.text)
            self.input_box.clear()
        else:
            # Wrong answer = game over
            self.scene_manager.set_scene(EndScene(self.scene_manager, self.score))

    # --------------------------------------------------
    # Drawing
    # --------------------------------------------------
    def draw(self, screen: pygame.Surface) -> None:
        """Draw game UI."""

        # Sprites (player, question)
        self.sprites.draw(screen)

        # Input box
        self.input_box.draw(screen)

        # Level and score
        level_text = self.info_font.render(
            f"Level: {self.level}   Score: {self.score}",
            True,
            COLOR_WHITE,
        )
        screen.blit(level_text, (20, 20))

        # Timer (turns red when low)
        timer_color = COLOR_WARNING if self.time_left < 2 else COLOR_WHITE
        timer_text = self.info_font.render(
            f"Time left: {self.time_left:.1f}s",
            True,
            timer_color,
        )
        timer_rect = timer_text.get_rect(topright=(WIDTH - 20, 20))
        screen.blit(timer_text, timer_rect)
