"""
Унисайз

Написать декоратор класса под названием sizer, который будет добавлять
в класс поле size. При обращении к этому полю возвращается len() объекта,
если объект имеет длину, иначе же abs() объекта, если от него вычисляется
модуль, и 0 в противном случае. Если в объекте присвоить этому полю некоторое
значение, будет возвращаться это значение до тех пор, пока поле не удалят.
"""


class AddSize:
    def __get__(self, obj, cls):
        res = 0
        if hasattr(obj, '__len__'):
            res = obj.__len__()
        elif hasattr(obj, '__abs__'):
            res = obj.__abs__()
        return res


def sizer(cls):
    cls.size = AddSize()
    return cls
