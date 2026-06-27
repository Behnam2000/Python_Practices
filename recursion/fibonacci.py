# In the Fibonacci sequence, each number is the sum of the two preceding ones: F(n) = F(n-1) + F(n-2)

def fibonacci(n):
    
    # 1. Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # 2. Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))