# Manual DSU — equivalent to sorted(words, key=len)
words = ["banana", "fig", "apple", "kiwi", "cherry"]

# 1. Decorate: pair each element with its key
decorated = [(len(w), w) for w in words]
# [(6, 'banana'), (3, 'fig'), (5, 'apple'), (4, 'kiwi'), (6, 'cherry')]

# 2. Sort: Python sorts tuples lexicorgraphical (key first, then element)
decorated.sort()
# [(3, 'fig'), (4, 'kiwi'), (5, 'apple'), (6, 'banana'), (6, 'cherry')]

# 3. Undecorate: strip the keys
result = [w for _, w in decorated]
print(result)


# Python's built-in key= does this automatically and efficiently
print(sorted(words, key=len))



#--------------------------------------------------
## Why DSU matters for expensive keys?:

import hashlib

words1 = ["banana", "fig", "apple", "kiwi", "cherry"] * 1000

# Without DSU: key function called O(n log n) times (at every comparison)
def expensive_key(w):
    return hashlib.sha256(w.encode()).hexdigest()

# With manual DSU: key function called exactly O(n) times
decorated1 = [(expensive_key(w), w) for w in words1]    # n calls
decorated1.sort()                                       # comparisons use precomputed keys
result1 = [w for _, w in decorated1]
print(result)