"""
Ящик с точками

Вводить вещественные числа x, y и z по три в строке через запятую,
считая их координатами точек (не менее одной тройки).
Конец ввода —пустая строка. Вывести минимальный объём содержащего
все точки параллелепипеда с рёбрамии, параллельными осям координат.
"""

coords = []

while str := input():
    coords.append(eval(str))

xmax, ymax, zmax, xmin, ymin, zmin = coords[0]*2

for x, y, z in coords[1:]:
    if x > xmax:
        xmax = x
    if x < xmin:
        xmin = x
    if y > ymax:
        ymax = y
    if y < ymin:
        ymin = y
    if z > zmax:
        zmax = z
    if z < zmin:
        zmin = z

print(abs(xmax - xmin)*abs(ymax - ymin)*abs(zmax - zmin))
