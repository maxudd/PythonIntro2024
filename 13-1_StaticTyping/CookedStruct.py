"""
Класс с преобразованием

Написать класс Cooked, который будет использовать аннотации к полям этого
класса в качестве функций преобразования значений во время присваивания их
полям. Исключения, которые могут возникнуть во время присваивания, не
обрабатывать. Предусмотреть также преобразование в строку, которое должно
возвращать перечень аннотированных полей (в порядке их появления в словаре
аннотаций и если они присутствуют в объекте) в формате ":имя=значение …:";
если таких полей нет, выводится "::".
"""


class Cooked:
    def __setattr__(self, name, value):
        if '__annotations__' in self.__dir__():
            annotations = self.__annotations__
            if name in annotations and callable(annotations[name]):
                value = annotations[name](value)
        super().__setattr__(name, value)

    def __str__(self):
        if '__annotations__' in self.__dir__():
            mid = ' '.join([f'{attr}={value}' for attr, value in
                            self.__dict__.items()
                            if attr in self.__annotations__])
        else:
            mid = ''
        return ':' + mid + ':'
