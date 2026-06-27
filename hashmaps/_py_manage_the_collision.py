import sys

d = {}

for i in range(10):
    d[i] = i
    print(f"size={len(d)} memory={sys.getsizeof(d)}")