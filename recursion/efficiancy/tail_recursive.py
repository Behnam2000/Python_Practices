# NOT tail-recursive: multiplication happens AFTER the recursive call returns
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # ← must wait for result to multiply by n


# Tail-recursive: accumulator carries the result; nothing left to do after return
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)    #  ← last operation is just the call


# ----------------------------------------------------
# convert tail-recursive functions to iterative loops
# ----------------------------------------------------

# Tail-recursive
def factorial_tail2(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail2(n - 1, acc * n)

# Equivalent iterative version (O(1) space)
def factorial_loop(n):
    acc = 1
    while n > 0:
        acc *= n
        n -= 1
    return acc

print(factorial_loop(100))  # no RecursionError !


# -----------------------------------------------------------
# Another tail-recursion-to-loop example - reversing a list
# -----------------------------------------------------------

# Tail-recursive
def reverse_tail(lst, acc=None):
    if acc is None: acc = []
    if not lst:
        return acc
    return reverse_tail(lst[1:], [lst[0]] + acc)

# Iterative equivalent
def reverse_loop(lst):
    acc = []

    for item in lst:
        acc = [item] + acc
    return acc