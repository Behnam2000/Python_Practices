# The simplest non-trivial recursive function. Defined mathematically as:
# n! = n × (n−1)!   for n ≥ 1
# 0! = 1             (base case)

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

print(factorial(5))
