"""
Частичный порядок

На вход подаются тройки чисел через запятую, последняя строка ввода — пустая.
Между тройками введён частичный порядок: (x₀, x₁, x₂) ≪ (y₀, y₁, y₂),
если ∃ i, j, k: (x₀, x₁, x₂) ≠ (yᵢ, yⱼ, yₖ) и x₀ ⩽ yᵢ, x₁ ⩽ yⱼ и
x₂ ⩽ yₖ, i≠j≠k. Отсортировать последовательность по убыванию,
по возможности не меняя следования элементов: каждая тройка должна быть
«не меньше» (т. е. утверждение A ≪ B неверно) следующих за ней.
Разрешается использовать устойчивый «тяжёлый» алгоритм сортировки
с квадратичной сложностью (например, сортировку выбором).
"""


def order(xs, ys):
    sort_xs = sorted(xs)
    sort_ys = sorted(ys)
    if sort_xs == sort_ys:
        return False
    for i in range(3):
        if sort_xs[i] > sort_ys[i]:
            break
    else:
        return True
    return False


lst = []

while s := input():
    lst.append(eval(s))

result = []

i = 0

while i < len(lst):
    current = lst[i]
    for elem in lst:
        if order(current, elem):
            i += 1
            break
    else:
        result.append(current)
        lst.remove(current)
        i = 0

result += lst

for elem in result:
    print(*elem, sep=', ')
