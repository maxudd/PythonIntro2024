"""
Бинарное возведение в степень

Написать функцию BinPow(), которая принимает три параметра:
python3-объект a,
натуральное число 0<N<1000000, и
некоторую ассоциативную бинарную функцию f().
Функция BinPow() реализует алгоритм бинарного возведения в степень
(кроме нулевой степени). Результатом BinPow(a, n, f) будет
применение f(x) к a n-1 раз.
"""


def BinPow(a, n, fun):
    if n == 1:
        return a
    if n % 2 == 1:
        return fun(a, BinPow(a, n - 1, fun))
    else:
        b = BinPow(a, n // 2, fun)
        return fun(b, b)


print(BinPow(2, 33, lambda a, b: a * b), 2**33)  # --> 8589934592 8589934592
print(BinPow("Se", 7, str.__add__))  # --> SeSeSeSeSeSeSe
