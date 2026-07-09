# Checking and Handling Deep Recursion Gracefully

import sys

def safe_factorial(n):
    if n > sys.getrecursionlimit() - 50:
        raise ValueError(f"n={n} is too large for recursive factorial; use iterative version")
    if n == 0:
        return 1
    return n * safe_factorial(n - 1)


# For every large n, fall back to iterative
def factorial_safe(n):
    try:
        return safe_factorial(n)
    except ValueError:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    

# print(safe_factorial(1000))    # ValueError  !

print(factorial_safe(1000))