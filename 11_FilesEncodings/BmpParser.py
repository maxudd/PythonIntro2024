import sys

content = sys.stdin.buffer
maybe_size = len(content.read())
content.seek(0)
header_id = content.read(2)
if header_id != b'BM':
    print('Not a Windows BMP')
    exit(0)
file_size = content.read(4)
if int.from_bytes(file_size, "little", signed=True) != maybe_size:
    print('Incorrect size')
    exit(0)
header = content.read(8)
dib_size = int.from_bytes(content.read(4), 'little')
dib_bytes_list = list(bytearray(content.read(dib_size - 4)))
if dib_size == 12:
    # print('ya old')
    width = abs(int.from_bytes(bytes(dib_bytes_list[0:2]), "little", signed=True))
    height = abs(int.from_bytes(bytes(dib_bytes_list[2:4]), "little", signed=True))
    bits_per_pixel = abs(int.from_bytes(bytes(dib_bytes_list[6:8]), "little", signed=True))
    comp_method = 0
    size = 0
elif dib_size in [16, 40, 52, 56, 64, 108, 124]:
    width = abs(int.from_bytes(bytes(dib_bytes_list[0:4]), "little", signed=True))
    height = abs(int.from_bytes(bytes(dib_bytes_list[4:8]), "little", signed=True))
    bits_per_pixel = abs(int.from_bytes(bytes(dib_bytes_list[10:12]), "little", signed=True))
    comp_method = int.from_bytes(bytes(dib_bytes_list[12:16]), "little")
    size = abs(int.from_bytes(bytes(dib_bytes_list[16:20]), "little", signed=True))
else:
    print('Incorrect header size')
    exit(0)

row_size = width * bits_per_pixel / 8
if ost := row_size % 4:
    row_size += 4 - ost
check_size = row_size*height
if check_size != size and size and size - check_size != 2:
    print('Incorrect image size')
    exit(0)

print(width, height, bits_per_pixel, comp_method, int(size - check_size))