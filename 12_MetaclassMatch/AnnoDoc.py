"""
Документация в аннотациях

Написать мета-класс AnnoDoc, который будет добавлять в произведённые им классы
такое свойство:
    * если data-атрибут класса аннотирован, и эта аннотация — строка, она
      считается его документацией
       * если у класса уже есть документация — добавляется туда с новой строки
       * если у класса не было документации — становится первой строкой
         документации класса
    * если у аннотированного строкой атрибута есть значение, тип этого
      значения становится его аннотацией
    * если аннотированный строкой атрибут ещё не задан, аннотация удаляется
Модифицировать поля .__doc__ и .__annotations__ (в обход inspect) разрешается.
"""


class AnnoDoc(type):
    def __init__(cls, name, parents, ns, **kwds):
        new_annot = {}
        for data, annot in cls.__annotations__.items():
            if isinstance(annot, str):
                if cls.__doc__ is None:
                    cls.__doc__ = data + ': ' + annot
                else:
                    cls.__doc__ += '\n' + data + ': ' + annot
                if hasattr(cls, data):
                    new_annot[data] = type(getattr(cls, data))
            else:
                new_annot[data] = cls.__annotations__[data]
        cls.__annotations__ = new_annot
        return super().__init__(name, parents, ns)
