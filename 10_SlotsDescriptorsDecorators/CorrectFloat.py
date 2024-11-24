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

class Fix:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            new_args = [round(ar, self.n) if isinstance(ar, float) else ar for ar in args]
            new_kwargs = {arg:value for (arg, value) in zip(kwargs.keys(), [round(ar, self.n) if isinstance(ar, float) else ar for ar in kwargs.values()])}
            res = fun(*new_args, **new_kwargs)
            return round(res, self.n) if isinstance(res, float) else res
        return wrapper
