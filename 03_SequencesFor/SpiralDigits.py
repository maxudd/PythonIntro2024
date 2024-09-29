"""
Цифры по спирали

Ввести целые M и N, вывести последовательность
0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде спирально (по часовой стрелке,
из верхнего левого угла) заполненной таблицы N*M (N строк, M столбцов).
Не забываем про то, что M и N могут быть чётными,
нечётными и неизвестно, какое больше.
"""

n, m = eval(input())
size = n*m

matrix = [[None]*n for _ in range(m)]

direction = 'right'

nums = list(range(10))
i_s = (nums*(size // 10 + 1))[:size]

x, y = 0, 0

left, right, up, down = 0, n - 1, 0, m - 1


for i in i_s:
    match direction:
        case 'right':
            matrix[y][x] = i
            if x == right:
                y += 1
                direction = 'down'
                up += 1
            else:
                x += 1
        case 'down':
            matrix[y][x] = i
            if y == down:
                x -= 1
                direction = 'left'
                right -= 1
            else:
                y += 1
        case 'left':
            matrix[y][x] = i
            if x == left:
                y -= 1
                direction = 'up'
                down -= 1
            else:
                x -= 1
        case 'up':
            matrix[y][x] = i
            if y == up:
                x += 1
                direction = 'right'
                left += 1
            else:
                y -= 1

for elem in matrix:
    print(*elem)
