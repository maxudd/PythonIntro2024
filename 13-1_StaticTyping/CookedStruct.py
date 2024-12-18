class Cooked:
    def __setattr__(self, name, value):
        if '__annotations__' in self.__dir__():
            annotations = self.__annotations__
            if name in annotations and callable(annotations[name]):
                value = annotations[name](value)
        super().__setattr__(name, value)
    def __str__(self):
        mid = ' '.join([f'{attr}={value}' for attr, value in self.__dict__.items() if attr in self.__annotations__]) if '__annotations__' in self.__dir__() else ''
        return ':' + mid + ':'
