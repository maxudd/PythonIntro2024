"""
Что-то вроде вектора

Написать класс vector, представляющий нечто, похожее на вектор.
Должна поддерживаться операция вывода в формате, представленном в примере,
конструирование из произвольной числовой последовательности ненулевой длины,
а также сложение и скалярное произведение с числовой последовательностью
такой же длины (в том числе с другим vector).
Скалярное произведение задаётся символом «@».
"""


class vector:

    def __init__(self, v):
        self.vec = v

    def __str__(self):
        return ':'.join([str(i) for i in self.vec])

    def __len__(self):
        return len(self.vec)

    def __add__(self, other):
        if isinstance(other, vector):
            return vector([s + o for s, o in zip(self.vec, other.vec)])
        else:
            return vector([s + o for s, o in zip(self.vec, other)])

    __radd__ = __add__

    def __matmul__(self, other):
        res = 0
        if isinstance(other, vector):
            for s, o in zip(self.vec, other.vec):
                res += s * o
        else:
            for s, o in zip(self.vec, other):
                res += s * o
        return res
