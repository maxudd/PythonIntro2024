"""
Прямоугольный класс

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_MatchSquare
"""


class Square:

    __match_args__ = "x", "y", "w"

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    @property
    def h(self):
        return self.w

    @property
    def s(self):
        return self.w ** 2

    @property
    def center(self):
        return self.x + self.w / 2, self.y + self.w / 2

    @h.setter
    def h(self, value):
        self.w = value

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
        self.x = self._center[0] - self.w / 2
        self.y = self._center[1] - self.w / 2
