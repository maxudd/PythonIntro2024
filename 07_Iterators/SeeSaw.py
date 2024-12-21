"""
Чёт-нечет

Написать генератор-функцию seesaw(sequence), которой на вход передаётся
итерируемая целочисленная последовательность, а конструируемый ею генератор
возвращает поочерёдно то чётный, то нечётный элемент последовательности
в порядке следования. Если элементы одного типа заканчиваются, возвращаются
только элементы другого.
"""

from itertools import zip_longest


def seesaw(seq):
    subseq1 = []
    subseq2 = []
    for i in seq:
        if i % 2:
            subseq2.append(i)
        else:
            subseq1.append(i)
    for e1, e2 in zip_longest(subseq1, subseq2):
        if e1 is not None:
            yield e1
        if e2 is not None:
            yield e2

# print(*seesaw(i//3 for i in range(1, 27, 2)))
# print(*seesaw([1] * 20))
# print(*seesaw(range(2, 40, 3)))
# print(*seesaw(range(3, 44, 3)))
