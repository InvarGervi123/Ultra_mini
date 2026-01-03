# core/app.py
"""
Main application class.

Responsible for:
- Initializing pygame
- Creating the window
- Running the main loop
- Delegating work to the current Scene (Menu / Game / End)

This file is intentionally SIMPLE.
No game logic is here – only flow control.
"""

import sys
import pygame

from core.constants import WIDTH, HEIGHT, FPS
from core.events import TICK_EVENT, FLASH_EVENT
from core.scene_manager import SceneManager
from ui.menu_scene import MenuScene


class GameApp:
    """
    The main application controller.

    This class owns:
    - the pygame window
    - the clock
    - the main loop

    It DOES NOT know game rules.
    It only forwards events/update/draw to the active Scene.
    """

    def __init__(self) -> None:
        """Initialize pygame, window, clock and scene manager."""
        pygame.init()

        # ---------- MUSIC (background) ----------
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music/background.mp3")
        pygame.mixer.music.set_volume(0.3)  # 0.0 - 1.0
        pygame.mixer.music.play(-1)         # -1 = loop forever
        # ---------------------------------------

        # Create window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Math Escape Game")

        # Clock controls FPS and delta-time
        self.clock = pygame.time.Clock()

        # Scene manager controls which screen is active
        self.scene_manager = SceneManager()

        # Start with MenuScene
        self.scene_manager.set_scene(MenuScene(self.scene_manager))

        # Start repeating custom events:
        # - tick every 100ms (game timer)
        # - flash every 700ms (visual effect / sprite blink)
        pygame.time.set_timer(TICK_EVENT, 100)
        pygame.time.set_timer(FLASH_EVENT, 700)

        self.running = True

    def run(self) -> None:
        """
        Main game loop.

        Order is ALWAYS:
        1) handle events
        2) update logic
        3) draw
        """
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # delta time in seconds

            # ---- Event handling ----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                # Forward event to current scene
                self.scene_manager.current_scene.handle_event(event)

            # ---- Update ----
            self.scene_manager.current_scene.update(dt)

            # ---- Draw ----
            self.screen.fill((20, 20, 30))  # clear screen
            self.scene_manager.current_scene.draw(self.screen)
            pygame.display.flip()

    def quit(self) -> None:
        """Exit the application cleanly."""
        pygame.mixer.music.stop()
        self.running = False
        pygame.quit()
        sys.exit()
