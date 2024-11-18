"""
Больше, чем минус

Написать класс NegExt, расширяющий унарный минус по следующей схеме:
    - Производный класс должен конструироваться с помощью
      class потомок(NegExt, родитель):
        - Если для родителя можно вызвать унарный минус, -потомок() возвращает
          то же, что и -родитель()
        - Если для родителя унарный минус не работает, но работает операция
          секционирования, -потомок() возвращает собственную секцию [1:-1]
        - В противном случае возвращается сам потомок 
    - Результат нужно во всех трёх случаях явно преобразовывать к типу потомка
      (предполагается, что такое преобразование возможно)
"""

class NegExt:
    def __neg__(self):
        parent = self.__class__.mro()[2]
        if hasattr(parent, '__neg__'):
            return self.__class__(parent.__neg__(self))
        elif hasattr(parent, '__getitem__'):
            try:
                return self.__class__(parent.__getitem__(self, slice(1, -1, None)))
            except KeyError:
                return self.__class__(self)
        else:
            return self.__class__(self)
    
# class nstr(NegExt, str):
#     pass
# class nnum(NegExt, int):
#     pass
# class ndict(NegExt, dict):
#     pass
# print(-nstr("Python"), -nnum(123), -ndict({1: 2, 3: 4}), --nstr("NegExt"))

