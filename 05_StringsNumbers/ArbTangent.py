"""
Тангенс

Ввести числа: рациональное A (целое или десятичная дробь) — угол из диапазона
от 1 до 99 градов (метрических градусов), и натуральное 4 ⩽ E ⩽ 1000 —
точность вычисления (в терминах контекста вычислений модуля Decimal —
поле perc). Вычислить значение тангенса с указанной точностью.
Число Пи (если оно вам понадобится) тоже надо вычислять!
"""

import decimal
from decimal import Decimal as dec


def pi_new():
    res = dec(13591409)
    fact1, fact3, fact6 = 1, 1, 1
    for k in range(1, decimal.getcontext().prec // 10):
        fact1 *= k
        fact3 *= 3*k * (3*k - 1) * (3*k - 2)
        for i in range(6*k - 5, 6*k + 1):
            fact6 *= i
        up = dec(-1)**k * fact6 * (13591409 + 545140134 * k)
        down = fact3 * fact1**3 * 640320**(3*k)
        res += up / down
    res *= (dec(10005).sqrt() / 4270934400)
    return dec(1) / res


def sin_new(x):
    curr = x
    prev = 0
    fact = 1
    pow_x = x
    n = 1
    sign = 1
    while curr != prev:
        prev = curr
        n += 2
        fact *= n * (n - 1)
        pow_x *= x**2
        sign *= -1
        curr += sign * pow_x / fact
    return curr


def cos_new(x):
    curr = 1
    prev = 0
    fact = 1
    pow_x = 1
    n = 0
    sign = 1
    while curr != prev:
        prev = curr
        n += 2
        fact *= n * (n - 1)
        pow_x *= x**2
        sign *= -1
        curr += sign * pow_x / fact
    return curr


angle_grad = dec(input())
decimal.getcontext().prec = int(input())

decimal.getcontext().prec += 5

angle_rad = angle_grad * pi_new() / 200

tan_new = sin_new(angle_rad) / cos_new(angle_rad)

decimal.getcontext().prec -= 5

print(+tan_new)
