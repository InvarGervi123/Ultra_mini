# main.py
"""
Entry point of the project.

Run:
    python main.py
"""

from core.app import GameApp


def main() -> None:
    """Create the app and start the main loop."""
    app = GameApp()
    app.run()


if __name__ == "__main__":
    main()
