# interfaces/question.py
"""
Question interface (abstract base class).

Every math question in the game must follow this interface.
This allows the game to work with ANY question type
without knowing its exact implementation.

This demonstrates:
- Abstraction
- Polymorphism
"""

from abc import ABC, abstractmethod


class BaseQuestion(ABC):
    """Abstract base class for a math question."""

    def __init__(self) -> None:
        self.text: str = ""    # what is shown to the player (e.g. "7 + 5 = ?")
        self.answer: int = 0   # correct answer

        # Generate the question immediately
        self.generate()

    @abstractmethod
    def generate(self) -> None:
        """
        Generate the question text and answer.

        Must set:
        - self.text
        - self.answer
        """
        raise NotImplementedError

    def is_correct(self, user_answer: str) -> bool:
        """
        Check if the user's answer is correct.

        user_answer: string from input box
        returns: True if correct, False otherwise
        """
        try:
            return int(user_answer) == self.answer
        except ValueError:
            # User entered something that is not a number
            return False
