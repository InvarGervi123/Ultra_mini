# interfaces/scene.py
"""
Scene interface (abstract base class).

Every scene in the game MUST implement:
- handle_event(event)
- update(dt)
- draw(screen)

This is the "contract" (Interface) for scenes.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import pygame


class BaseScene(ABC):
    """Abstract base class for all scenes (Menu / Game / End)."""

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle a single pygame event (keyboard/mouse/custom events)."""
        raise NotImplementedError

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update logic. dt is seconds since last frame."""
        raise NotImplementedError

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the scene to the given screen surface."""
        raise NotImplementedError
