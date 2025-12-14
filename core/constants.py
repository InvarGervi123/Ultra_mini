# core/constants.py
"""
Global constants used across the project.

Keeping constants here:
- avoids magic numbers
- improves readability
- makes changes easy (one place only)
"""

# ---------------- Window ----------------
WIDTH: int = 900
HEIGHT: int = 500
FPS: int = 60

# ---------------- Colors (RGB) ----------------
COLOR_BG = (20, 20, 30)
COLOR_WHITE = (255, 255, 255)
COLOR_BUTTON = (40, 40, 40)
COLOR_BUTTON_BORDER = (200, 200, 200)
COLOR_PLAYER = (0, 200, 255)
COLOR_WARNING = (220, 80, 80)

# ---------------- Gameplay ----------------
START_TIME_LIMIT: float = 6.0   # seconds for first question
MIN_TIME_LIMIT: float = 1.5     # minimum allowed time per question
TIME_DECAY: float = 0.92        # each level multiplies time by this value
