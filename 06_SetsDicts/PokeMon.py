"""
Покемоны

Участники некоторой карточной игры владеют несколькими колодами, из которых
они составляют пачку — набор попарно различающихся карт. Каждая колода имеет
номер; колоды с одинаковыми номерами содержат совпадающие наборы карт.
Ввести строки вида "имя игрока / номер колоды" (колода принадлежит игроку)
или "номер колоды / название карты" (карта входит в колоду); последняя строка
пустая. Вывести в алфавитном порядке имена всех игроков, чья пачка наибольшая.
Имена игроков и названия карт не могут начинаться с цифры.
"""

from collections import defaultdict

dictcolplay, dictcolcard, dictplay = defaultdict(list), defaultdict(list), defaultdict(int)

while st := input():
    a, b = st.split(' / ')
    if a.isnumeric():
        dictcolcard[int(a)] += [b]
    else:
        dictcolplay[a] += [int(b)]

for player, cols in dictcolplay.items():
    cardlist = []
    for col in cols:
        cardlist += dictcolcard[col]
    dictplay[player] = len(set(cardlist))

print(*sorted([player for player, cards in dictplay.items() if cards == max(dictplay.values())]), sep='\n')
