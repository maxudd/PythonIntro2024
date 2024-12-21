"""
Интервалы

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_BraceDecode
"""

import re
from fractions import Fraction as fr


def interval(diap):
    open_pat = r'([\[|\(])\s*'
    num = r'(-)?\s*(\d+\.\d+|\d+)\s*'
    mid_pat = r'(\.\.(([1-9]\d+|[2-9])+)\.\.|\.{2,})\s*'
    close_pat = r'([\]|\)])'
    ult_pattern = re.compile(fr'^{open_pat}{num}{mid_pat}{num}{close_pat}$')
    ult_res = ult_pattern.search(diap)
    if not ult_res:
        return
    open, sign_st, st, mid, leng, _, sign_en, en, close = ult_res.groups()
    if leng:
        length = int(leng) - 1
    else:
        length = len(mid) - 1
    start = fr(sign_st + st) if sign_st else fr(st)
    end = fr(sign_en + en) if sign_en else fr(en)

    step = (end - start) / length
    if open == '(':
        if close == ')':
            end -= step
        else:
            start += step
    else:
        if close == ')':
            end -= step

    while start != end:
        yield start
        start += step
    yield end

# from itertools import islice

# print(*interval("[1.....10)"))
# print(*interval("1..2"))
# print(*interval("[1.5]"))
# print(*interval("(1..5]"))
# print(*interval("[1.1......5.5]"))
# print(*interval("[1.1..123..5.5]"))
# print(*islice(interval("[1.1..123..5.5]"),120,123))
# print(*islice(interval("[1.1..1123..5.5]"),1120,1123))
# print(*islice(interval("[7..11123..-15]"),11120,11123))
# print(*islice(interval("[7..31123..15]"),21120,21123))
# print(*interval("[.7..31123..15]"))
# print(*interval("[+7..31123..15]"))
# print(*interval("[7..-31123..15]"))
# print(*interval("[7..+31123..15]"))
# print(*interval("[7..311.23..15]"))
# print(*interval("[7..311.23..15]]"))
# print(*interval("[7..311.23..15]?"))
