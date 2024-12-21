"""
Случайности

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_RndSwissknife
"""

import random
from collections.abc import Sequence, Iterable


def rnd(a, b=None):
    match a, b:
        case int(), None:
            return random.randint(0, a)
        case int(), int():
            return random.randint(a, b)
        case float(), (int() | float()):
            return random.uniform(a, b)
        case str(), (None | str()):
            return random.choice(a.split(b))
        case str(), int():
            start = random.randint(0, len(a) - b)
            return a[start: (start + b)]
        case (Sequence() | Iterable()), None:
            return random.choice(list(a))
        case (Sequence() | Iterable()), int():
            return random.choices(list(a), k=b)

# rnd(7)
# rnd(100, 500)
# rnd(1.3, 10)
# rnd(list('edg ehog'))
# random.seed(123)
# print(*(rnd(3, 5) for i in range(11)))
# print(rnd(5))
# print(*(round(rnd(3., 5), 4) for i in range(4)))
# print(*(rnd("Substring", 4) for i in range(4)))
# print(*(rnd("We won oewn wow") for i in range(5)))
# print(*(rnd("We won oewn wow", "wo") for i in range(4)))
# print(*(rnd(range(10)) for i in range(12)))
# print(*(rnd({1, 3, 5, 7}) for i in range(12)))
# print(*(rnd(range(10), 3) for i in range(4)))
# print(*(rnd(enumerate("qwe"), 1) for i in range(5)))
