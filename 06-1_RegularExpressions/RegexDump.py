import re

pattern = input()
strs = []

while s := input():
    strs.append(s)

for str1 in strs:
    pat = re.compile(fr'{pattern}')
    res = pat.search(str1)
    if res:
        startpos, _ = res.span()
        print(f'{startpos}: {res.group()}')
        for gr, substr in enumerate(res.groups()):
            if substr:
                print(f'{gr+1}/{res.start(gr+1)}: {substr}')
        for gr, substr in res.groupdict().items():
            if substr:
                print(f'{gr}/{res.start(gr)}: {substr}')
    else:
        print('<NONE>')

