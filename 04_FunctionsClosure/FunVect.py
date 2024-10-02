"""
Вектор функций

Написать функцию superposition(funmod, funseq), которая принимает
два параметра — функцию funmod() от одного переменного, и последовательность
funseq[] функций от одного переменного. superposition() возвращает также
список функций funres[], каждая из которых представляет собой суперпозицию
вида funres[i](x) ≡ funmod(funseq[i](x))
"""

from math import *


def superposition(funmod, funseq):
    funres = []
    for i in range(len(funseq)):
        funres.append(lambda x, j=i: funmod(funseq[j](x)))
    return funres


F, G = superposition(abs, (sin, cos))
print(F(-1), G(-1), F(2), G(2))
# -> 0.8414709848078965 0.5403023058681398 0.9092974268256817 0.4161468365...
