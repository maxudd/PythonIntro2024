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
    
def strictsort(seq: Sortable, key: Callable[[Comparable], Comparable] = defkey) -> Sortable:
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key(seq[j]) > key(seq[j + 1]):
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

# c: Sortable = [6, 1, 4, 2, 7, 2, 8, 3]
# print(*strictsort(c))
# print(*strictsort([6., 1., 4., 2., 7., 2., 8., 3.]))
# print(*strictsort(["234", "sdf23452345234gg", "45645674567", "ASDASD"]))
# print(*strictsort([(1, 2, 4, 9), (2, 7, 4, 6, 8), (1,), (8, 9, 23), (7, 2, 1)]))
# print(defkey(9), defkey("999"))
# c: Sortable = [7j, 2j, 3j]
# defkey(iter("123"))
# print(*strictsort({1: 2, 3: 4}))