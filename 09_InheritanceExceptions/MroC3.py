"""
MRO C3

Написать программу, на вход которой подаётся синтаксически верный код на
ЯП Python, состоящий только из объявления классов верхнего уровня, без пустых
строк и многострочных констант. В наследовании используются только уже
определённые ранее в этом коде классы. На выходе программа должна отчитаться,
допустимо ли наследование, которое (возможно) встретилось в коде (с точки
зрения MRO C3), и вывести "Yes" или "No".
"""

import re
        
def merge(seqs):
    res = []
    i = 0
    while i < len(seqs):
        if seqs[i]:
            cand = seqs[i][0]
        else:
            i += 1
            continue
        if any([el.index(cand) > 0 if cand in el else False for el in seqs]):
            cand = None
            i += 1
            continue
        else:
            res.append(cand)
            for seq in seqs:
                if seq and seq[0] == cand:
                    del seq[0]
    return res if cand else None

linears = dict()

while line := input():
    if res := re.search(r'^class (\w+)(\((.+)\))?:', line):
        cls_name, _, parents = res.groups()
        if not parents:
            linears[cls_name] = [cls_name]
        else:
            parent_list = parents.split(', ')
            merge_res = merge([*[linears[x][:] for x in parent_list], parent_list])
            if not merge_res:
                print('No')
                break
            else:
                linears[cls_name] = [cls_name] + merge_res
else:
    print('Yes')
