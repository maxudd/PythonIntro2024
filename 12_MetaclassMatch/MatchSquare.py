class Square:
    __match_args__ = "x", "y", "w"
    def __init__(self, x, y, w):
        self._x = x
        self._y = y
        self._w = w
        self._h = w
        self._s = self._w ** 2
        self._center = self._x + self._w / 2, self._y + self._h / 2

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h
    
    @property
    def s(self):
        return self._s

    @property
    def center(self):
        return self._center
    
    @x.setter
    def x(self, value):
        self._x = value
        self._center = self._x + self._w / 2, self._y + self._h / 2

    @y.setter
    def y(self, value):
        self._y = value
        self._center = self._x + self._w / 2, self._y + self._h / 2

    @w.setter
    def w(self, value):
        self._w = value
        self.x = self._center[0] - self._w / 2
        self.y = self._center[1] - self._h / 2

    @h.setter
    def h(self, value):
        self._h = value
        self.x = self._center[0] - self._w / 2
        self.y = self._center[1] - self._h / 2
    
    @s.setter
    def s(self, value):
        pass

    @center.setter
    def center(self, value):
        match value:
            case a, b, c, d:
                self._center = a + c, b + d              
            case _, _:
                self._center = value
        self._x = self._center[0] - self._w / 2
        self._y = self._center[1] - self._h / 2
