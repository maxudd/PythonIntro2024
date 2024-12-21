"""
Размер архива

Написать программу, которой на стандартный ввод подаётся tar-архив в виде
шестнадцатеричного дампа (последовательность шестнадцатеричных цифр, возможно,
разделённых пробелами и переводами строки), а на выходе она показывает
количество и суммарный объём хранящихся в нём файлов, если их распаковать.
"""

import tarfile
import sys
import io

file = io.BytesIO(bytes.fromhex(sys.stdin.read()))

with tarfile.open(fileobj=file) as arhiv:
    files = list(filter(lambda x: x.isfile(), arhiv))
    files_count = len(files)
    files_size = sum([tfile.size for tfile in files])

print(files_size, files_count)
