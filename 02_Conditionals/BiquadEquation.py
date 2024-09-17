"""
Биквадратное уравнение

Ввести через запятую три числа: a, b и c,
вывести все вещественные решения уравнения ax⁴+bx²+c=0.
При a ≠ 0 это уравнение превращается в биквадратное.
Решения выводить через пробел в порядке возрастания, если решений нет,
вывести 0, если их бесконечно много — -1.
"""

from math import sqrt

a, b, c = eval(input())

if a == 0:
    if b == 0:
        print('-1' if c == 0 else '0')
    elif c == 0:
        print('0')
    else:
        x2 = -c/b
        print('0') if x2 < 0 else print(-sqrt(x2), sqrt(x2))
else:
    disc = b*b - 4*a*c
    fp = -b/(2*a)
    sp = sqrt(disc)/(2*a)
    if disc < 0:
        print('0')
    elif disc == 0:
        print('0') if fp <= 0 else print(-sqrt(fp), sqrt(fp))
    else:
        r1 = fp + sp
        r2 = fp - sp
        res = []
        if r1 > 0:
            res.append(sqrt(r1))
            res.append(-sqrt(r1))
        elif r1 == 0:
            res.append(0)
        if r2 > 0:
            res.append(sqrt(r2))
            res.append(-sqrt(r2))
        elif r2 == 0:
            res.append(0)
        if r1 < 0 and r2 < 0:
            print('0')
        else:
            for r in sorted(set(res)):
                print(r, end=' ')
            print()