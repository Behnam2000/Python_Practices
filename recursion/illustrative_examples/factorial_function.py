def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Trace for factorial(5):
# factorial(5) = 5 * factorial(4)
#              = 5 * 4 * factorial(3)
#              = 5 * 4 * 3 * factorial(2)
#              = 5 * 4 * 3 * 2 * factorial(1)
#              = 5 * 4 * 3 * 2 * 1 * factorial(0)
#              = 5 * 4 * 3 * 2 * 1 * 1
#              = 120

print(factorial(5))   # 120


# --------------------
# Compared to the Iterative version:
# -------------------------------------

def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iter(5))