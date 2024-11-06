"""
Смешение языцей

Написать функцию mix(…) от произвольного количества параметров-объектов.
Функция воспринимает объекты как инкапсулированные пространства имён и
возвращает объект, содержащий объединение полей всех объектов-параметров.
Поля, чьи имена начинаются на "_", и все callable-поля (методы и функции)
отбрасываются. Если в некоторых объектах поля имеют одинаковые имена,
используется значение последнего из параметров. Дополнительно у возвращаемого
объекта переопределяется __str__(): она возвращает строку вида
"поле=значение, поле=значение, …", в которой имена полей отсортированы
в алфавитном порядке.
"""


class Mixed:

    def __init__(self, *args):
        for cl in args:
            for elem in dir(cl):
                attr_value = getattr(cl, elem)
                if not elem.startswith('_') and not callable(attr_value):
                    setattr(self, elem, attr_value)

    def __str__(self):
        res = []
        for elem in dir(self):
            attr_value = getattr(self, elem)
            if not elem.startswith('_') and not callable(attr_value):
                res.append(elem + '=' + str(attr_value))
        return ', '.join(res)


def mix(*args):
    return Mixed(*args)

# class C:
#     imag = 100500
# e = mix(range(3, 4, 5), 6, C)
# print(e)
# print(e.denominator, e.imag, e.numerator, e.real, e.start, e.step, e.stop)
