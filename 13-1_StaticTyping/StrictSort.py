"""
Строгая сортировка

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_StrictSort
"""

from typing import Protocol, Self
from collections.abc import Sized, MutableSequence, Callable


class Comparable(Protocol):
    def __lt__(self, other: Self) -> bool:
        pass


type Sortable = MutableSequence[Comparable]


def defkey(element: Comparable) -> Comparable:
    if isinstance(element, Sized):
        return element.__len__()
    else:
        return element


def strictsort(seq: Sortable,
               key: Callable[[Comparable], Comparable] = defkey) -> Sortable:
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key(seq[j]) > key(seq[j + 1]):
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
