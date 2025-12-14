# logic/storage.py
"""
High score storage (file handling + error handling).

This module is OPTIONAL for the game to run,
but gives BONUS points in the assignment.

Responsibilities:
- Load high score from file
- Save high score to file
- Handle errors safely (file missing / corrupted)
"""

import json
from pathlib import Path

# File path for saving high score
FILE_PATH = Path("data/highscore.json")


def load_highscore() -> int:
    """
    Load high score from file.

    Returns:
        int: saved high score
             0 if file does not exist or is invalid
    """
    try:
        if not FILE_PATH.exists():
            return 0

        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return int(data.get("highscore", 0))

    except (json.JSONDecodeError, ValueError, OSError):
        # File exists but is broken / unreadable
        return 0


def save_highscore(score: int) -> None:
    """
    Save new high score to file.

    Creates directory if needed.
    """
    try:
        FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump({"highscore": score}, file)

    except OSError:
        # If saving fails, we silently ignore
        # (game should never crash because of file IO)
        pass
