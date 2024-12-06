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

