"""
Выпуклый мнгогоугольник

Ввести построчно 300 ⩾ N > 2 пар целых чисел, разделённых запятой (ввод
оканчивается пустой строкой). Считая пары координатами точек, проверить,
могут ли эти точки в определённом порядке быть вершинами выпуклого
N-угольника. Вывести True, если могут, или False, если нет.
"""

from math import atan2


def cross_product(point1, point2, point3):
    p1x, p1y = point1
    p2x, p2y = point2
    p3x, p3y = point3
    return (p2x - p1x) * (p3y - p1y) - (p2y - p1y) * (p3x - p1x)


def mass_center(points):
    n = len(points)
    xsum = sum(x for x, y in points)
    ysum = sum(y for x, y in points)
    return xsum / n, ysum / n


def is_convex(points):
    n = len(points)
    prev = 0
    curr = 0
    for i in range(n):
        curr = cross_product(points[i], points[(i + 1) % n], points[(i + 2) % n])
        if curr:
            if curr * prev < 0:
                return False
            else:
                prev = curr
    return True


points = []
while st := input():
    points.append(list(eval(st)))

cent = mass_center(points)

new_points = list(map(lambda x: [x[0] - cent[0], x[1] - cent[1]], points))

new_points.sort(key=lambda x: atan2(x[1], x[0]))

print('True' if is_convex(new_points) else 'False')
