"""
Три квадрата

Ввести произвольную последовательность (не обязательно кортеж) натуральных
чисел, не превышающих 200000. Вывести, сколько среди них различных чисел,
являющихся суммой трёх квадратов натуральных чисел.
"""

from math import sqrt, floor, ceil

seq = set(eval(input()))

intsqrt = lambda x: int(sqrt(x)) + 1

M = max(seq)

squares = {i*i + j*j + k*k for i in range(1, intsqrt(M)) for j in range(i, intsqrt(M - i*i)) for k in range(j, intsqrt(M - i*i - j*j))}

print(len(seq & squares))