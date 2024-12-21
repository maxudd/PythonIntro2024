"""
Киберколбаса

Написать класс Sausage, имитирующий киберколбасу. Киберколбаса может быть
проинициализирована нулём значений (создаётся один батон с фаршем "pork!"),
одним (фарш типа str) и двумя (фарш, и объём типа Fraction). Длина целого
батона киберколбасы — 12 символов фарша и 2 символа оболочки. Колбаса
единичного объёма — это один полный батон, более, чем единичного — это
несколько батонов (последний, возможно, неполон). Неполный батон
заканчивается срезом. Киберколбаса поддерживает операции умножения и
деления на целое неотрицательное число, сложение и вычитание с другой
киберколбасой (фарш результата совпадает с фаршем первого операнда), а
также взятие абсолютного значения (возвращается объём). Отрицательного
объёма не бывает, в этом случае он делается нулевым. Если объём киберколбасы
нулевой, батон считается пустым. При выводе округлять двенадцатые доли
батона в сторону ближайшего меньшего.
"""

from fractions import Fraction as fr
from itertools import batched, cycle, islice, chain


def help(cont, num):
    return batched(islice(chain.from_iterable(cycle(cont)), num), 12)


class Sausage:

    def __init__(self, strr='pork!', v=1):
        self.strr = strr
        self.v = fr(v)
        self.full_content = ''.join(islice(cycle(self.strr), 12))

    def __str__(self):
        if self.v < fr(1/12):
            return '/|\n||\n||\n||\n\\|'
        num = (12 * self.v).__floor__()
        up = '/' + '\\/'.join(list(map(lambda x: ''.join(x),
                                       batched(islice(cycle('-'), num), 12))))
        mid = '|' \
            + '||'.join([''.join(x) for x in help(self.full_content, num)]) \
            + '|\n'

        down = '\\' \
            + '/\\'.join([''.join(x) for x in
                          batched(islice(cycle('-'), num), 12)])
        if num % 12:
            up += '|'
            down += '|'
        else:
            up += '\\'
            down += '/'
        return up + '\n' + mid*3 + down

    def __add__(self, other):
        return Sausage(self.strr, self.v + other.v)

    def __sub__(self, oth):
        return Sausage(self.strr, self.v - oth.v if self.v - oth.v > 0 else 0)

    def __mul__(self, other):
        return Sausage(self.strr, self.v * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return Sausage(self.strr, self.v / other)

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return self.v
