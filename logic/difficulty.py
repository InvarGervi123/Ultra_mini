# logic/difficulty.py
"""
Difficulty handling for the game.

This module contains ONLY one responsibility:
- calculate the time limit for the next level

Keeping it separate makes the game logic cleaner
and very easy to explain.
"""

from core.constants import TIME_DECAY, MIN_TIME_LIMIT


def next_time_limit(current_limit: float) -> float:
    """
    Calculate the next time limit.

    Each level:
    - time is multiplied by TIME_DECAY
    - but never goes below MIN_TIME_LIMIT

    Example:
        6.0 -> 5.52 -> 5.07 -> ...
    """
    new_limit = current_limit * TIME_DECAY

    if new_limit < MIN_TIME_LIMIT:
        return MIN_TIME_LIMIT

    return new_limit
