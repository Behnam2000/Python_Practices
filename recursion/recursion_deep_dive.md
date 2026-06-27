# Python Recursion — Deep Dive with Examples

---

## 1. What Is Recursion?

Recursion is when a function solves a problem by calling itself on a smaller version of the same problem. It is not magic — it is just a different way to express repetition compared to `for`/`while` loops, and in many cases it produces cleaner, more readable code.

The simplest possible recursive function you can write is a countdown:

```python
def countdown(n):
    if n <= 0:          # base case
        print("Go!")
    else:
        print(n)
        countdown(n - 1)    # recursive case — calls itself with a smaller n

countdown(3)
# 3
# 2
# 1
# Go!
```

The same logic written iteratively:

```python
def countdown_iter(n):
    while n > 0:
        print(n)
        n -= 1
    print("Go!")
```

Both produce identical output. The recursive version delegates the "rest of the work" to a smaller version of itself instead of using a loop. This pattern — solve a tiny piece, then hand the rest off — is the core idea behind every recursive function.

---

## 2. Core Components: Base Cases and Recursive Cases

Every recursive function must have two clearly defined parts.

### Base Cases

A base case is the condition under which the function stops calling itself and returns a direct (non-recursive) answer. Without a base case, the function never terminates.

```python
# DANGER: no base case — runs forever (until Python raises RecursionError)
def infinite_sum(n):
    return n + infinite_sum(n - 1)   # will never stop

# Safe version with a base case
def sum_down(n):
    if n == 0:          # base case
        return 0
    return n + sum_down(n - 1)   # recursive case

print(sum_down(5))   # 15
```

A function can also have multiple base cases:

```python
def is_palindrome(s):
    if len(s) <= 1:          # base case 1: empty string or single char
        return True
    if s[0] != s[-1]:        # base case 2: mismatch found
        return False
    return is_palindrome(s[1:-1])  # recursive case: strip outer chars

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
```

### Recursive Cases

The recursive case is where the function calls itself with a simpler or smaller input. Each recursive call **must** move closer to a base case — if it does not, you get infinite recursion.

```python
def factorial(n):
    # --- recursive case progression for n=4 ---
    # factorial(4) → 4 * factorial(3)
    # factorial(3) → 3 * factorial(2)
    # factorial(2) → 2 * factorial(1)
    # factorial(1) → 1 * factorial(0)
    # factorial(0) → 1  ← base case reached
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

The key invariant: every step reduces `n` by 1, so the base case `n == 0` is guaranteed to be hit.

---

## 3. Mechanics: The Call Stack and Activation Records

Understanding what happens under the hood removes a lot of the mystery from recursion.

### Activation Records (Frames)

Each time Python calls a function — including a recursive call to itself — it creates a new **frame** (also called an activation record) on the **call stack**. This frame stores:

- The function's local variables for that specific call
- The current position in the function's code
- A reference back to the caller's frame

You can actually inspect frames at runtime:

```python
import sys

def show_depth():
    """Returns the current call-stack depth."""
    frame = sys._getframe()
    depth = 0
    while frame:
        depth += 1
        frame = frame.f_back
    return depth

def factorial(n):
    print(f"  entering factorial({n}), stack depth = {show_depth()}")
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    print(f"  leaving  factorial({n}), returning {result}")
    return result

factorial(4)
```

Output:
```
  entering factorial(4), stack depth = 3
  entering factorial(3), stack depth = 4
  entering factorial(2), stack depth = 5
  entering factorial(1), stack depth = 6
  entering factorial(0), stack depth = 7
  leaving  factorial(0), returning 1
  leaving  factorial(1), returning 1
  leaving  factorial(2), returning 2
  leaving  factorial(3), returning 6
  leaving  factorial(4), returning 24
```

### Visualizing the Call Stack

Here is what the call stack looks like while computing `factorial(4)`, just before hitting the base case:

```
 ┌─────────────────────────────────────────┐
 │  factorial(0)  — returns 1              │  ← top (most recent call)
 ├─────────────────────────────────────────┤
 │  factorial(1)  — suspended, n=1        │
 ├─────────────────────────────────────────┤
 │  factorial(2)  — suspended, n=2        │
 ├─────────────────────────────────────────┤
 │  factorial(3)  — suspended, n=3        │
 ├─────────────────────────────────────────┤
 │  factorial(4)  — suspended, n=4        │  ← bottom (original call)
 └─────────────────────────────────────────┘
```

Once `factorial(0)` returns `1`, each suspended frame resumes in reverse order, multiplying its `n` with the return value from below.

You can also use `traceback.print_stack()` to print the live call stack at any point during a recursive execution.

---

## 4. Classifications of Recursion

### Linear Recursion

A function that makes **at most one** recursive call per invocation.

**Example 1 — Factorial:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   # exactly one recursive call
```

**Example 2 — Summing a list:**
```python
def sum_list(lst):
    if not lst:             # base case: empty list
        return 0
    return lst[0] + sum_list(lst[1:])   # one recursive call

print(sum_list([3, 7, 1, 9]))  # 20
```

**Example 3 — Reversing a string:**
```python
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("hello"))  # "olleh"
```

Linear recursion generally has **O(n)** time and **O(n)** space (one frame per call).

---

### Binary Recursion

A function that makes **exactly two** recursive calls per invocation. This is common in divide-and-conquer algorithms.

**Example 1 — Summing a sequence by splitting in half:**
```python
def binary_sum(data, start, stop):
    """Divide the sequence in half; sum each half recursively."""
    if start >= stop:           # base case: empty slice
        return 0
    if start == stop - 1:       # base case: single element
        return data[start]
    mid = (start + stop) // 2
    left  = binary_sum(data, start, mid)   # recursive call 1
    right = binary_sum(data, mid, stop)    # recursive call 2
    return left + right

data = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_sum(data, 0, len(data)))   # 36
```

**Example 2 — Drawing an English ruler (the classic textbook example):**
```python
def draw_line(length, label=""):
    print("-" * length + (" " + label if label else ""))

def draw_interval(center_length):
    """Draw the tick marks between two major ticks."""
    if center_length > 0:
        draw_interval(center_length - 1)   # upper half
        draw_line(center_length)
        draw_interval(center_length - 1)   # lower half (two calls!)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, "0")
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

draw_ruler(2, 3)
```

Output:
```
--- 0
-
--
-
--- 1
-
--
-
--- 2
```

Binary recursion has **O(log n)** depth but can produce **O(n)** total work overall (e.g., merge sort is O(n log n)).

---

### Multiple Recursion

A function that makes **three or more** recursive calls per invocation. Combinatorial problems are the classic use case.

**Example 1 — Generating all permutations:**
```python
def permutations(lst):
    """Generate all orderings of lst. Makes len(lst) recursive calls."""
    if len(lst) <= 1:
        return [lst[:]]       # base case: only one ordering
    result = []
    for i in range(len(lst)):
        # Pick element i as the first, permute the rest
        first   = lst[i]
        rest    = lst[:i] + lst[i+1:]
        for perm in permutations(rest):   # recursive call for each choice
            result.append([first] + perm)
    return result

print(permutations([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**Example 2 — Power set (all subsets):**
```python
def power_set(lst):
    """Generates 2^n subsets."""
    if not lst:
        return [[]]   # base case: only the empty set
    first = lst[0]
    rest  = power_set(lst[1:])           # recursive call
    with_first    = [[first] + s for s in rest]
    without_first = rest
    return with_first + without_first

print(power_set([1, 2, 3]))
# [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

Multiple recursion can be expensive — permutations of n elements requires O(n!) calls.

---

## 5. Classic Illustrative Examples

### Factorial

The simplest non-trivial recursive function. Defined mathematically as:

```
n! = n × (n−1)!   for n ≥ 1
0! = 1             (base case)
```

```python
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
```

Compared to the iterative version:

```python
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iter(5))   # 120
```

Both are O(n) time and the recursive version is O(n) space (due to stack frames), while the iterative version is O(1) space.

---

### Binary Search

Binary search is an excellent example of **linear recursion** applied to efficiency. Given a **sorted** sequence, it locates a target in O(log n) time by halving the search range at each step.

```python
def binary_search(data, target, low=0, high=None):
    if high is None:
        high = len(data) - 1

    if low > high:               # base case 1: target not found
        return -1

    mid = (low + high) // 2

    if data[mid] == target:      # base case 2: target found
        return mid
    elif data[mid] < target:     # target must be in the right half
        return binary_search(data, target, mid + 1, high)
    else:                        # target must be in the left half
        return binary_search(data, target, low, mid - 1)

data = [2, 5, 7, 10, 14, 19, 25, 31, 40]

print(binary_search(data, 14))   # 4
print(binary_search(data, 99))   # -1
```

**Trace for searching 19 in the list above (indices 0–8):**
```
Call 1: low=0, high=8, mid=4 → data[4]=14 < 19, go right
Call 2: low=5, high=8, mid=6 → data[6]=25 > 19, go left
Call 3: low=5, high=5, mid=5 → data[5]=19 == 19 ✓ return 5
```

Only 3 calls to search 9 elements — this is O(log n) in action.

---

### File System Traversal

Operating systems represent directories recursively (a directory contains files and possibly more directories). Recursive functions naturally mirror this structure.

```python
import os

def list_directory(path, indent=0):
    """Recursively print all files and folders under path."""
    name = os.path.basename(path)
    print(" " * indent + ("📁 " if os.path.isdir(path) else "📄 ") + name)
    if os.path.isdir(path):
        for entry in sorted(os.listdir(path)):
            full = os.path.join(path, entry)
            list_directory(full, indent + 4)   # recursive call for each item

# list_directory("/path/to/your/folder")
```

**Example output:**
```
📁 project
    📁 src
        📄 main.py
        📄 utils.py
    📁 tests
        📄 test_main.py
    📄 README.md
```

A useful variation — computing total directory size recursively:

```python
def dir_size(path):
    """Return total size in bytes of all files under path."""
    if os.path.isfile(path):                     # base case: it's a file
        return os.path.getsize(path)
    total = 0
    for entry in os.listdir(path):               # recursive case: directory
        total += dir_size(os.path.join(path, entry))
    return total
```

---

### Trees (Binary Trees)

A binary tree is defined recursively: it is either empty (`None`) or a node with a value, a left subtree, and a right subtree — where each subtree is itself a binary tree.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# Build a small tree:
#         10
#        /  \
#       5    15
#      / \     \
#     3   7    20

root = TreeNode(10,
    TreeNode(5, TreeNode(3), TreeNode(7)),
    TreeNode(15, None, TreeNode(20))
)
```

The three fundamental recursive tree traversals:

```python
def inorder(node):
    """Left → Root → Right  (produces sorted order for a BST)"""
    if node is None:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

def preorder(node):
    """Root → Left → Right  (useful for copying/serializing a tree)"""
    if node is None:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    """Left → Right → Root  (useful for deleting a tree)"""
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")

print("Inorder:  ", end=""); inorder(root);   print()  # 3 5 7 10 15 20
print("Preorder: ", end=""); preorder(root);  print()  # 10 5 3 7 15 20
print("Postorder:", end=""); postorder(root); print()  # 3 7 5 20 15 10
```

Other useful tree operations that are naturally recursive:

```python
def tree_height(node):
    """Height = longest path from root to a leaf."""
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def tree_sum(node):
    if node is None:
        return 0
    return node.val + tree_sum(node.left) + tree_sum(node.right)

print(tree_height(root))   # 3
print(count_nodes(root))   # 6
print(tree_sum(root))      # 60
```

---

## 6. Efficiency and Pitfalls

### Exponential Inefficiency — The Fibonacci Example

The naive recursive Fibonacci is the classic example of what NOT to do:

```python
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
```

The problem becomes clear when you draw the call tree for `fib(6)`:

```
                        fib(6)
                     /          \
               fib(5)           fib(4)
              /      \          /     \
         fib(4)    fib(3)   fib(3)  fib(2)
         /    \    /    \   /    \
      fib(3) fib(2) ...  ...   ...
      ...
```

`fib(4)` is computed **twice**, `fib(3)` is computed **three times**, `fib(2)` five times… The total number of calls grows as O(2ⁿ). For `n=50`, this would require over a quadrillion calls.

```python
import time

start = time.time()
print(fib_naive(35))         # 9227465
print(f"Time: {time.time() - start:.2f}s")   # several seconds!
```

---

### Memory Overhead and Stack Overflow

Each frame on the call stack consumes memory. A very deep recursion can exhaust the stack:

```python
def deep(n):
    if n == 0:
        return 0
    return 1 + deep(n - 1)

try:
    deep(5000)
except RecursionError as e:
    print(f"Caught: {e}")
# Caught: maximum recursion depth exceeded
```

This is why it matters that recursive cases make meaningful progress toward the base case, and why extremely deep recursions are often better rewritten iteratively.

---

### Memoization (Caching)

Memoization solves the redundant-computation problem by storing results the first time they are computed and returning the cached value on subsequent calls.

**Manual memoization with a dictionary:**

```python
def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]       # cache hit — return immediately
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

print(fib_memo(100))   # 354224848179261915075  (instant!)
```

**Using `functools.lru_cache` (the Pythonic way):**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))     # 354224848179261915075
print(fib(1000))    # works instantly (result is enormous)

# Inspect the cache stats
print(fib.cache_info())
# CacheInfo(hits=998, misses=1001, maxsize=None, currsize=1001)
```

With memoization, Fibonacci drops from O(2ⁿ) to **O(n)** time and O(n) space — each value is computed exactly once.

**Comparing all three approaches:**

```python
import time
from functools import lru_cache

# Naive — O(2^n)
def fib_naive(n):
    if n <= 1: return n
    return fib_naive(n-1) + fib_naive(n-2)

# Memoized — O(n)
@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1: return n
    return fib_cached(n-1) + fib_cached(n-2)

# Iterative — O(n) time, O(1) space
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 35
t0 = time.perf_counter(); fib_naive(n);  print(f"Naive:   {time.perf_counter()-t0:.4f}s")
t0 = time.perf_counter(); fib_cached(n); print(f"Cached:  {time.perf_counter()-t0:.6f}s")
t0 = time.perf_counter(); fib_iter(n);   print(f"Iterative: {time.perf_counter()-t0:.6f}s")
# Naive:     ~2.5s
# Cached:    ~0.000010s
# Iterative: ~0.000003s
```

---

### Tail Recursion

A function is **tail-recursive** when the recursive call is the **very last operation** in the function — nothing is done with the return value except pass it up.

```python
# NOT tail-recursive: multiplication happens AFTER the recursive call returns
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   # ← must wait for result to multiply by n

# Tail-recursive: accumulator carries the result; nothing left to do after return
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)   # ← last operation is just the call
```

In a tail-recursive function, the current frame is not needed after the recursive call, so in theory the compiler/interpreter can **reuse** the frame (tail-call optimization / TCO), keeping memory usage constant.

**Important Python note:** Python does **not** perform tail-call optimization by design (Guido van Rossum has explicitly rejected it). So a tail-recursive Python function still creates a new frame for each call and will still hit the recursion limit.

The practical takeaway is: **convert tail-recursive functions to iterative loops** in Python:

```python
# Tail-recursive
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)

# Equivalent iterative version (O(1) space)
def factorial_loop(n):
    acc = 1
    while n > 0:
        acc *= n
        n   -= 1
    return acc

print(factorial_loop(1000))   # no RecursionError!
```

Another tail-recursion-to-loop example — reversing a list:

```python
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
```

---

## 7. Python System Constraints

### The Recursion Limit

Python enforces a hard cap on the number of simultaneously active frames to prevent runaway recursion from crashing the interpreter or consuming all available memory.

```python
import sys

print(sys.getrecursionlimit())    # 1000 on most systems
```

When the limit is exceeded:

```python
def count_down(n):
    return count_down(n - 1)

try:
    count_down(10000)
except RecursionError as e:
    print(f"RecursionError: {e}")
# RecursionError: maximum recursion depth exceeded
```

### Changing the Limit

```python
import sys

sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())   # 5000
```

**Caution:** raising this limit raises the risk of a genuine stack overflow at the OS level (which is much harder to catch than a Python `RecursionError`). It is generally safer to redesign deeply recursive algorithms to be iterative.

### Why Python Does Not Optimize Tail Calls

Python intentionally preserves every stack frame because the traceback (the list of frames shown when an error occurs) is a critical debugging tool. Eliminating frames would make tracebacks incomplete and harder to understand. This is a deliberate trade-off by the language designers — explicitness and debuggability over memory optimization.

### Checking and Handling Deep Recursion Gracefully

```python
import sys

def safe_factorial(n):
    if n > sys.getrecursionlimit() - 50:
        raise ValueError(f"n={n} is too large for recursive factorial; use iterative version")
    if n == 0:
        return 1
    return n * safe_factorial(n - 1)

# For very large n, fall back to iterative
def factorial_safe(n):
    try:
        return safe_factorial(n)
    except ValueError:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```

---

## Summary Table

| Topic | Key Idea | Time | Space |
|---|---|---|---|
| Linear recursion | One recursive call | O(n) | O(n) |
| Binary recursion | Two recursive calls | O(n) | O(log n) |
| Multiple recursion | Many recursive calls | O(2ⁿ)+ | O(n) |
| Fibonacci (naive) | Exponential redundancy | O(2ⁿ) | O(n) |
| Fibonacci (memoized) | Cache results | O(n) | O(n) |
| Binary search | Halve search range | O(log n) | O(log n) |
| Tree traversal | Visit all nodes | O(n) | O(h) — h = height |
| Tail recursion (iterative) | Reuse frame / loop | O(n) | O(1) |
