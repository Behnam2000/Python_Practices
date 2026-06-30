def deep(n):
    if n == 0:
        return 0
    return 1 + deep(n - 1)

try:
    deep(5000)
except RecursionError as e:
    print(f"Caught: {e}")

# it will throws Caught: maximum recursion depth exceeded.