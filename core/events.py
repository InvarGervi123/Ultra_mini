# core/events.py
"""
Custom pygame events used in the game.

Why custom events?
- Cleaner logic
- No need to check timers manually everywhere
- Required by the assignment (event_custom)

All custom events must start from pygame.USEREVENT.
"""

import pygame

# Fired every fixed interval (used for timers / UI updates)
TICK_EVENT: int = pygame.USEREVENT + 1

# Fired when time for a question is over
TIME_UP_EVENT: int = pygame.USEREVENT + 2

# Additional custom event used for visual effects (blinking player)
# Demonstrates using more than one custom event/timer in the app
FLASH_EVENT: int = pygame.USEREVENT + 3
