# Manual memoization with a dictionary:

def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]        # cache hit - return immediately
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

print(fib_memo(100))   # 354224848179261915075  (instant!)

#-----------------------------------------------------------------------
# Using functools.lru_cache (the Pythonic way):

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))         # 354224848179261915075
print(fib(1000))        # works instantly (result is enormous)

# Inspect the cache stats
print(fib.cache_info())

# With memoization, Fibonacci drops from O(2ⁿ) to O(n) time and O(n) space — each value is computed exactly once.


#-------------------------------------------------------------------------
# Comparing all three approaches

import time
# from functools import lru_cache

# Naive - O(2^n)
def fib_naive(n):
    if n <= 1: return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Memoized - O(n)
@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1: return n
    return fib_cached(n - 1) + fib_cached(n - 2)

# Iterative - O(n) time, O(1) space
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 35
t0 = time.perf_counter(); fib_naive(n);  print(f"Naive:   {time.perf_counter()-t0:.4f}s")
t0 = time.perf_counter(); fib_cached(n); print(f"Cached:  {time.perf_counter()-t0:.6f}s")
t0 = time.perf_counter(); fib_iter(n);   print(f"Iterative: {time.perf_counter()-t0:.6f}s")