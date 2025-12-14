# logic/questions.py
"""
Concrete implementations of math questions.

This file contains VERY SIMPLE question types.
No tricks, no complex logic – easy to explain in defense.

All question classes inherit from BaseQuestion.
"""

import random
from interfaces.question import BaseQuestion


class AddQuestion(BaseQuestion):
    """
    Addition question.
    Example: 7 + 5 = ?
    """

    def generate(self) -> None:
        a = random.randint(1, 20)
        b = random.randint(1, 20)

        self.text = f"{a} + {b} = ?"
        self.answer = a + b


class MulQuestion(BaseQuestion):
    """
    Multiplication question.
    Example: 6 * 4 = ?
    """

    def generate(self) -> None:
        a = random.randint(2, 10)
        b = random.randint(2, 10)

        self.text = f"{a} × {b} = ?"
        self.answer = a * b


class MixedQuestion(BaseQuestion):
    """
    Mixed question.
    Randomly chooses between addition and multiplication.

    Demonstrates POLYMORPHISM:
    GameScene works with BaseQuestion,
    not caring which concrete type this is.
    """

    def generate(self) -> None:
        if random.choice([True, False]):
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            self.text = f"{a} + {b} = ?"
            self.answer = a + b
        else:
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            self.text = f"{a} × {b} = ?"
            self.answer = a * b
