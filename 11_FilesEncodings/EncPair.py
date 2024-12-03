import sys

codings = ['KOI8-R', 'CP1251', 'CP866', 'MACCYRILLIC', 'ISO-8859-5', 'CP855']

text = sys.stdin.buffer.read()
cs = []
for c2 in codings:
    for c1 in codings:
        for init_coding in codings:
            if c1 != c2:
                try:
                    old = text.decode(c2).encode(c1).decode(init_coding)
                    if 'Зимбабве' in old:
                        print(old)
                        exit(0)
                except Exception:
                    pass

