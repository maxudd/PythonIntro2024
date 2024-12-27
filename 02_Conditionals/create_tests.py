import re
import os

prog = input()

with open(prog, 'r') as raw:
    text = raw.read()
    numtests = re.findall(r'Тест #(\d+)', text)
    ins = re.findall(r'Входные данные: размер \d+ ---\n(.*)', text)
    outs = re.findall(r'Правильный ответ: размер \d+ ---\n(.*)', text)

os.system(f'mkdir {prog}_tests')

for i in numtests:
    with open(f'{prog}_tests/{i}.in', 'w') as inn:
        inn.write(ins[int(i)-1])
    with open(f'{prog}_tests/{i}.out', 'w') as out:
        out.write(f'{outs[int(i)-1]}\n')
