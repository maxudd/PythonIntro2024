import tarfile
import sys
import io

file = io.BytesIO(bytes.fromhex(sys.stdin.read()))

with tarfile.open(fileobj=file) as arhiv:
    files = list(filter(lambda x: x.isfile(), arhiv))
    files_count = len(files)
    files_size = sum([tfile.size for tfile in files])

print(files_size, files_count)