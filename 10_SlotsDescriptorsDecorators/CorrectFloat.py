"""
Фиксированная точность

Написать класс-параметрический декоратор Fix(n), с помощью которого все
вещественные (как позиционные, так и именные) параметры произвольной
декорируемой функции, а также её возвращаемое значение, округляются до
n-го знака после запятой (1 ⩽ n ⩽ 16). Если какие-то параметры функции
оказались не вещественными, или не вещественно возвращаемое значение, эти
объекты не меняются.
"""

from functools import wraps


def rnd(x, n):
    return round(x, n) if isinstance(x, float) else x


class Fix:
    def __init__(self, n):
        self.n = n

    def __call__(self, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            new_args = [rnd(ar, self.n) for ar in args]
            ks, vs = kwargs.keys(), kwargs.values()
            kwds = {a: v for a, v in zip(ks, [rnd(ar, self.n) for ar in vs])}
            res = fun(*new_args, **kwds)
            return rnd(res, self.n)
        return wrapper
