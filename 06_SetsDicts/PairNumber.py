"""
Количество пар

Вводится текст, состоящий из «слов» (последовательностей непробельных
символов), разделённых последовательностями пробельных символов. Последняя
строка пустая. Посчитать и вывести, сколько различных последовательных пар
слов (без учёта порядка) встречается в тексте.
"""

ll = []

while st := input():
    ll += st.split()

pairset = {frozenset(ll[i:i+2]) for i in range(len(ll)-1)}

print(len(pairset))
