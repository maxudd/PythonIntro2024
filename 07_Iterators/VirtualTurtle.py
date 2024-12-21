"""
Примитивная черепашка

Написать параметрическую генератор-функцию turtle(coord, direction),
описывающую движение «черепахи» по координатной плоскости.
coord — это кортеж из двух целочисленных начальных координат,
direction описывает первоначальное направление (0 — восток, 1 — север,
2 — запад, 3 — юг).
Координаты увеличиваются на северо-восток.
Генератор принимает три команды:
"f" (переход на 1 шаг вперёд),
"l" (поворот против часовой стрелки на 90°),
"r" (поворот по часовой стрелке на 90°)
    и возвращает текущие координаты черепахи.
"""


def turtle(coord, direction):
    x, y = coord
    res = yield x, y
    while res:
        match res:
            case 'f':
                match direction:
                    case 0:
                        x += 1
                    case 1:
                        y += 1
                    case 2:
                        x -= 1
                    case 3:
                        y -= 1
            case 'l':
                direction = (direction + 1) % 4
            case 'r':
                direction = (direction - 1) % 4
        res = yield x, y


# robo = turtle((0, 0), 1)
# start = next(robo)
# for c in "flfrffrffr":
    # print(*robo.send(c))
