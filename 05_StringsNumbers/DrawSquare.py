"""
Рисуем квадраты

Написать функцию squares(w,h,(X,Y,s,c),...) со следующими параметрами: w и h —
ширина и высота «экрана», за которыми следуют 0 или больше 4-элементных
последовательностей вида (X,Y,s,c), где X и Y — координаты левого верхнего
угла квадрата, s — длина его стороны (не меньше 1), а c — символ которым он
заполняется на экране. Функция должна выводить прямоугольник из h*w точек,
на котором соответствующими символами «нарисованы» квадраты соответствующих
размеров в соответствующих местах. Координаты левого верхнего угла поля — 0,0;
координаты растут вправо вниз.
Проверять, что квадраты не выходят за границы поля, не надо.
"""


def squares(w, h, *args):
    win = [['.']*w for _ in range(h)]

    for X, Y, s, c in args:
        for i in range(Y, Y + s):
            win[i][X:X+s] = [c]*s

    for elem in win:
        print(*elem, sep='')


# squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))
# squares(1,1)
# squares(14,14,(0,0,14,'#'),(7,7,3,'.'))
# squares(113, 113, (1,1,95,'@'), (20,30,50,'!'), (40,5,44,'#'), (80,110,2,'/'))