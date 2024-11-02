import re
from fractions import Fraction as fr

def interval(diap):
    ultimate_pattern = re.compile(r'^([\[|\(])\s*(-)?\s*(\d+\.\d+|\d+)\s*(\.\.(([1-9]\d+|[2-9])+)\.\.|\.{2,})\s*(-)?\s*(\d+\.\d+|\d+)\s*([\]|\)])$')
    ult_res = ultimate_pattern.search(diap)
    if not ult_res:
        return
    open_bracket, sign_st, st, mid, leng, _, sign_en, en, close_bracket = ult_res.groups()
    if leng:
        length = int(leng) - 1
    else:
        length = len(mid) - 1
    start = fr(sign_st + st) if sign_st else fr(st)
    end = fr(sign_en + en) if sign_en else fr(en)

    step = (end - start) / length
    if open_bracket == '(':
        if close_bracket == ')':
            end -= step
        else:
            start += step
    else:
        if close_bracket == ')':
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
