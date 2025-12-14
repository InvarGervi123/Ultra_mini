# core/scene_manager.py
"""
SceneManager controls which screen (Scene) is currently active.

A "Scene" is one full screen:
- MenuScene
- GameScene
- EndScene

The app always calls:
    current_scene.handle_event(event)
    current_scene.update(dt)
    current_scene.draw(screen)

This keeps the main loop simple and readable.
"""

from interfaces.scene import BaseScene


class SceneManager:
    """Holds and switches the current Scene."""

    def __init__(self) -> None:
        self.current_scene: BaseScene | None = None

    def set_scene(self, scene: BaseScene) -> None:
        """Switch to a new scene."""
        self.current_scene = scene
