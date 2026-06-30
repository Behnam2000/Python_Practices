# The naive recursion Fibonnaci is the classic example of what NOT to do: 
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# The problem becomes clear when you draw the call tree for fib(6):

#                         fib(6)
#                      /          \
#                fib(5)           fib(4)
#               /      \          /     \
#          fib(4)    fib(3)   fib(3)  fib(2)
#          /    \    /    \   /    \
#       fib(3) fib(2) ...  ...   ...
#       ...

# fib(4) is computed twice, fib(3) is computed three times, 
#  fib(2) five times… The total number of calls grows as O(2ⁿ).
#    For n=50, this would require over a quadrillion calls.

import time

start = time.time()
print(fib_naive(35))
print(f"Time: {time.time() - start:.2f}s")