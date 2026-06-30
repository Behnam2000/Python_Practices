def count_down(n):
    return count_down(n - 1)

try:
    count_down(10000)
except RecursionError as e:
    print(f"RecursionError: {e}")
# RecursionError: maximum recursion depth exceeded

# ------------------
# Changing the limit
# ------------------

import sys

print(sys.getrecursionlimit())  # 1000 on most systems
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())  # 5000
