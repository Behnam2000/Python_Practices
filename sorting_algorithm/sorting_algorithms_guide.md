# Sorting Algorithms in Python — A Deep Dive

---

## How We Evaluate Sorting Algorithms

Before diving into the algorithms themselves, it helps to understand the three lenses we use to compare them:

| Criterion | What it means |
|---|---|
| **Time complexity** | How the number of operations grows with input size `n` |
| **Space complexity** | How much extra memory is needed beyond the input |
| **Stability** | Does it preserve the original order of *equal* elements? |

### Quick Example: Why Stability Matters

```python
students = [("Alice", "B"), ("Bob", "A"), ("Charlie", "B")]
# Sorted by grade (A first, then B)
# A STABLE sort will guarantee Alice comes before Charlie
# because they had the same grade and Alice appeared first
```

---

## Summary Table

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | **O(n)** | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | **O(1)** | ❌ |
| Bucket Sort | O(n+N) | O(n+N) | O(n²) | O(n+N) | ✅ |
| Radix Sort | O(d·n) | O(d·n) | O(d·n) | O(n+k) | ✅ |

---

## Part 1 — Quadratic Time Algorithms O(n²)

### 1. Bubble Sort

**How it works:** It makes repeated passes through the list. On each pass, it compares neighboring elements and swaps them if they are out of order. After pass `i`, the `i`-th largest element is guaranteed to be in its final position (it has "bubbled up" to the right end).

**Step-by-step trace on `[5, 3, 8, 1]`:**

```
Pass 1:
  [5, 3, 8, 1]  →  compare 5 & 3  → swap  → [3, 5, 8, 1]
  [3, 5, 8, 1]  →  compare 5 & 8  → ok    → [3, 5, 8, 1]
  [3, 5, 8, 1]  →  compare 8 & 1  → swap  → [3, 5, 1, 8]  ← 8 is now in place

Pass 2:
  [3, 5, 1, 8]  →  compare 3 & 5  → ok    → [3, 5, 1, 8]
  [3, 5, 1, 8]  →  compare 5 & 1  → swap  → [3, 1, 5, 8]  ← 5 is now in place

Pass 3:
  [3, 1, 5, 8]  →  compare 3 & 1  → swap  → [1, 3, 5, 8]  ← done!
```

**Implementation:**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: if no swaps happened, the list is already sorted
        if not swapped:
            break
    return arr

# Examples
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([1, 2, 3, 4, 5]))               # [1, 2, 3, 4, 5] — only 1 pass needed!
print(bubble_sort([5, 4, 3, 2, 1]))               # [1, 2, 3, 4, 5] — worst case
```

**Key points:**
- The `swapped` flag is an important optimization — if no swaps occurred in a full pass, the array is sorted. This makes the best case O(n) for already-sorted data.
- Bubble sort is **stable** — equal elements are never swapped, so their relative order is preserved.
- Despite its simplicity, it is rarely used in practice because it performs O(n²) comparisons even when only a few elements are out of place.

---

### 2. Selection Sort

**How it works:** Divide the array into a "sorted" portion on the left and "unsorted" on the right. On each step, scan the entire unsorted portion to find the minimum element, then swap it into the next position of the sorted portion.

**Step-by-step trace on `[29, 10, 14, 37, 13]`:**

```
Step 1: unsorted = [29, 10, 14, 37, 13]  → min is 10 at index 1 → swap with index 0
        → [10 | 29, 14, 37, 13]

Step 2: unsorted = [29, 14, 37, 13]       → min is 13 at index 4 → swap with index 1
        → [10, 13 | 29, 14, 37]

Step 3: unsorted = [29, 14, 37]           → min is 14 at index 2 → swap with index 2
        → [10, 13, 14 | 29, 37]

Step 4: unsorted = [29, 37]               → min is 29, already in place
        → [10, 13, 14, 29 | 37]

Done:  [10, 13, 14, 29, 37]
```

**Implementation:**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element of the unsorted part is the minimum
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Examples
print(selection_sort([29, 10, 14, 37, 13]))  # [10, 13, 14, 29, 37]
print(selection_sort([5, 5, 5, 5]))           # [5, 5, 5, 5] — only 4 swaps total
```

**Counting swaps:**

```python
def selection_sort_count(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, swaps

arr = [64, 25, 12, 22, 11]
sorted_arr, swap_count = selection_sort_count(arr)
print(f"Sorted: {sorted_arr}, Total swaps: {swap_count}")
# Sorted: [11, 12, 22, 25, 64], Total swaps: 4
```

**Key points:**
- Selection sort makes at most **n-1 swaps** — ideal when writes are expensive (e.g., flash memory).
- It always performs O(n²) comparisons, regardless of how sorted the input is.
- It is **not stable** by default — swapping can disrupt the order of equal elements.

---

### 3. Insertion Sort

**How it works:** Maintain a sorted "left portion" of the array. For each new element, shift larger elements in the sorted portion to the right to make room, then insert the new element into its correct position.

**Step-by-step trace on `[4, 3, 2, 10, 12, 1, 5, 6]`:**

```
Start:       [4 | 3, 2, 10, 12, 1, 5, 6]
Insert 3:    [3, 4 | 2, 10, 12, 1, 5, 6]   (shift 4 right)
Insert 2:    [2, 3, 4 | 10, 12, 1, 5, 6]   (shift 4, 3 right)
Insert 10:   [2, 3, 4, 10 | 12, 1, 5, 6]   (already in place)
Insert 12:   [2, 3, 4, 10, 12 | 1, 5, 6]   (already in place)
Insert 1:    [1, 2, 3, 4, 10, 12 | 5, 6]   (shift everything right)
Insert 5:    [1, 2, 3, 4, 5, 10, 12 | 6]
Insert 6:    [1, 2, 3, 4, 5, 6, 10, 12]
```

**Implementation:**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # The element to be inserted
        j = i - 1
        # Shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key      # Insert the key in its correct position
    return arr

# Examples
print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))  # [1, 2, 3, 4, 5, 6, 10, 12]
print(insertion_sort([1, 2, 3, 4, 5]))              # O(n) — already sorted, no shifts!
print(insertion_sort(["banana", "apple", "cherry"])) # ['apple', 'banana', 'cherry']
```

**Why it shines on nearly-sorted data:**

```python
import time

def time_sort(sort_fn, arr):
    import copy
    a = copy.deepcopy(arr)
    start = time.perf_counter()
    sort_fn(a)
    return time.perf_counter() - start

n = 10_000
sorted_data = list(range(n))
random_data = sorted_data[::-1]  # Worst case for insertion sort

print(f"Nearly sorted: {time_sort(insertion_sort, sorted_data):.6f}s")
print(f"Reversed:      {time_sort(insertion_sort, random_data):.6f}s")
# Nearly sorted will be drastically faster!
```

**Key points:**
- Best case is O(n) when data is already sorted — no inner loop iterations occur.
- It is **stable** and **in-place**.
- It is the algorithm of choice for small arrays and is used internally by Timsort (Python's built-in) for small sub-sequences.

---

## Part 2 — Log-Linear Time Algorithms O(n log n)

### 4. Merge Sort

**How it works:** A classic divide-and-conquer algorithm.
1. **Divide:** Split the array in half recursively until each piece has 1 element (already sorted).
2. **Conquer:** Merge pairs of sorted pieces together by comparing their front elements and taking the smaller one each time.

**Visualization of the divide & merge:**

```
          [38, 27, 43, 3, 9, 82, 10]
           /                       \
    [38, 27, 43, 3]           [9, 82, 10]
      /          \               /      \
  [38, 27]    [43, 3]       [9, 82]    [10]
   /    \      /    \        /    \
 [38]  [27]  [43]  [3]    [9]  [82]
   \    /      \    /        \    /
  [27, 38]   [3, 43]       [9, 82]
       \          /               \
    [3, 27, 38, 43]            [9, 10, 82]
              \                    /
           [3, 9, 10, 27, 38, 43, 82]
```

**Implementation:**

```python
def merge_sort(arr):
    # Base case: a list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (merge)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare the front of each sorted half and take the smaller
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= ensures stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Examples
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([1]))                           # [1]
print(merge_sort([]))                            # []
print(merge_sort(["grape", "apple", "mango"]))   # ['apple', 'grape', 'mango']
```

**Tracing the merge step:**

```python
def merge_verbose(left, right):
    """Merge with step-by-step output"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        print(f"  Comparing {left[i]} vs {right[j]}")
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

merge_verbose([3, 27, 38, 43], [9, 10, 82])
# Comparing 3 vs 9   → take 3
# Comparing 27 vs 9  → take 9
# Comparing 27 vs 10 → take 10
# Comparing 27 vs 82 → take 27
# Comparing 38 vs 82 → take 38
# Comparing 43 vs 82 → take 43
# Remaining [82] appended
```

**Key points:**
- Guaranteed O(n log n) in all cases — no worst case degradation.
- The downside is O(n) extra memory needed for the merged temporary arrays.
- It is **stable**.
- Preferred when stability is required, or when sorting linked lists (no random access needed).

---

### 5. Quick Sort

**How it works:** Also divide-and-conquer, but divides by value instead of by position.
1. **Choose a pivot** element from the array.
2. **Partition:** rearrange so all elements smaller than the pivot are to its left, and all greater are to its right. The pivot is now in its final sorted position.
3. **Recurse** on both sub-arrays.

**Partition example with pivot = 10 on `[3, 6, 8, 10, 1, 2, 1]`:**

```
Pivot: 10
Less than 10:    [3, 6, 8, 1, 2, 1]
Equal to 10:     [10]
Greater than 10: []
→ [3, 6, 8, 1, 2, 1] + [10] + []
Recurse on left...
```

**Implementation (clean functional style):**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]   # Choose middle element as pivot
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))  # [1, 1, 2, 3, 6, 8, 10]
```

**Implementation (in-place with Lomuto partition scheme):**

```python
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]   # Use last element as pivot
    i = low - 1         # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort_inplace(arr))  # [1, 5, 7, 8, 9, 10]
```

**The worst case problem and how to avoid it:**

```python
# Worst case: sorted or reverse-sorted input with a naive pivot choice
# [1, 2, 3, 4, 5] with pivot=first element → O(n²)

# Fix 1: Random pivot
import random
def quick_sort_random(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]   # Swap random with last
        pivot_idx = partition(arr, low, high)
        quick_sort_random(arr, low, pivot_idx - 1)
        quick_sort_random(arr, pivot_idx + 1, high)
    return arr

# Fix 2: Median-of-three pivot
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    # Sort low, mid, high and pick middle as pivot
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # Place pivot at high-1
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    return arr[high - 1]
```

**Key points:**
- Average case O(n log n), but O(n²) in the worst case (nearly sorted data with bad pivot).
- In practice, it is often faster than Merge Sort due to better cache performance.
- It is **not stable** in its standard form.
- It can be implemented **in-place** using O(log n) stack space for recursion.

---

### 6. Heap Sort

**How it works:** Uses a **binary max-heap** — a tree where every parent is greater than its children.
1. **Heapify:** Transform the array into a max-heap. The largest element ends up at index 0.
2. **Extract:** Swap the root (maximum) with the last element, reduce the heap size by 1, and restore the heap property. Repeat.

**Understanding a Max-Heap:**

```
Array: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

As a tree:
           16
         /    \
       14      10
      /  \    /  \
     8    7  9    3
    / \  /
   2   4 1

Parent of index i → index (i-1)//2
Left child of i  → 2i + 1
Right child of i → 2i + 2
```

**Implementation:**

```python
def heapify(arr, n, i):
    """
    Maintain the max-heap property for subtree rooted at index i.
    n = current heap size (elements beyond n are sorted).
    """
    largest = i          # Assume root is largest
    left    = 2 * i + 1
    right   = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)   # Recursively fix the affected subtree


def heap_sort(arr):
    n = len(arr)

    # Phase 1: Build max-heap (start from last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Move max to end
        heapify(arr, i, 0)                 # Restore heap for remaining elements

    return arr


print(heap_sort([12, 11, 13, 5, 6, 7]))   # [5, 6, 7, 11, 12, 13]
print(heap_sort([1]))                       # [1]
print(heap_sort([3, 1, 4, 1, 5, 9, 2, 6])) # [1, 1, 2, 3, 4, 5, 6, 9]
```

**Using Python's `heapq` (min-heap):**

```python
import heapq

def heap_sort_builtin(arr):
    heapq.heapify(arr)           # O(n) build
    return [heapq.heappop(arr) for _ in range(len(arr))]   # O(n log n) extract

print(heap_sort_builtin([3, 1, 4, 1, 5, 9, 2, 6]))  # [1, 1, 2, 3, 4, 5, 6, 9]
```

**Key points:**
- Guaranteed O(n log n) in all cases — no worst case trap like Quick Sort.
- O(1) space — it is fully **in-place**.
- It is **not stable**.
- It has poor cache performance compared to Quick Sort, making it slower in practice despite the same asymptotic complexity.

---

## Part 3 — Linear Time Algorithms O(n)

These algorithms bypass the O(n log n) lower bound by not comparing elements directly, instead using their values as keys.

### 7. Bucket Sort

**How it works:**
1. Divide the input range into `N` equally spaced "buckets".
2. Distribute each input element into the appropriate bucket based on its value.
3. Sort each bucket individually (often with insertion sort).
4. Concatenate all buckets in order.

**Step-by-step example on `[0.72, 0.17, 0.39, 0.26, 0.55, 0.81, 0.03]` with 4 buckets:**

```
Range [0, 1) split into 4 buckets: [0, 0.25), [0.25, 0.5), [0.5, 0.75), [0.75, 1.0)

Distribute:
  Bucket 0 [0.00 – 0.25): [0.17, 0.03]
  Bucket 1 [0.25 – 0.50): [0.39, 0.26]
  Bucket 2 [0.50 – 0.75): [0.72, 0.55]
  Bucket 3 [0.75 – 1.00): [0.81]

Sort each bucket:
  Bucket 0: [0.03, 0.17]
  Bucket 1: [0.26, 0.39]
  Bucket 2: [0.55, 0.72]
  Bucket 3: [0.81]

Concatenate: [0.03, 0.17, 0.26, 0.39, 0.55, 0.72, 0.81]
```

**Implementation:**

```python
def bucket_sort(arr, num_buckets=None):
    if not arr:
        return arr

    n = len(arr)
    num_buckets = num_buckets or n

    min_val, max_val = min(arr), max(arr)
    # Avoid division by zero for uniform arrays
    range_val = (max_val - min_val) or 1

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for val in arr:
        if val == max_val:
            idx = num_buckets - 1
        else:
            idx = int((val - min_val) / range_val * num_buckets)
        buckets[idx].append(val)

    # Sort each bucket and collect
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))   # insertion_sort(bucket) for integers
    return result


# Float example (ideal use case)
floats = [0.72, 0.17, 0.39, 0.26, 0.55, 0.81, 0.03]
print(bucket_sort(floats))   # [0.03, 0.17, 0.26, 0.39, 0.55, 0.72, 0.81]

# Integer example
ints = [42, 17, 89, 23, 55, 3, 78]
print(bucket_sort(ints, num_buckets=5))  # [3, 17, 23, 42, 55, 78, 89]
```

**Key points:**
- Runs in O(n + N) where N is the number of buckets; approaches O(n) when N ≈ n.
- Works best when data is **uniformly distributed** across a known range.
- Performance degrades to O(n²) in the worst case if all elements land in the same bucket.

---

### 8. Radix Sort

**How it works:** Sorts integers (or strings) one "digit" at a time, from the **least significant digit (LSD)** to the most significant, using a stable counting sort at each pass.

**Step-by-step example on `[170, 45, 75, 90, 802, 24, 2, 66]`:**

```
Original:   [170, 45, 75, 90, 802, 24, 2, 66]

Pass 1 (ones digit):
  Digits:      0,   5,  5,  0,   2,  4, 2,  6
  Buckets:  0:[170,90]  2:[802,2]  4:[24]  5:[45,75]  6:[66]
  After:    [170, 90, 802, 2, 24, 45, 75, 66]

Pass 2 (tens digit):
  Digits:      7,  9,  0,  0,  2,  4,  7,  6
  Buckets:  0:[802,2]  2:[24]  4:[45]  6:[66]  7:[170,75]  9:[90]
  After:    [802, 2, 24, 45, 66, 170, 75, 90]

Pass 3 (hundreds digit):
  Digits:      8,  0,  0,  0,  0,  1,  0,  0
  Buckets:  0:[2,24,45,66,75,90]  1:[170]  8:[802]
  After:    [2, 24, 45, 66, 75, 90, 170, 802]  ← SORTED!
```

**Implementation:**

```python
def counting_sort_by_digit(arr, exp):
    """Stable sort of arr by the digit at position exp (1, 10, 100, ...)"""
    n = len(arr)
    output = [0] * n
    count  = [0] * 10   # Digits 0–9

    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Accumulate counts (convert to positions)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array in reverse (to maintain stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output


def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr


print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))  # [2, 24, 45, 66, 75, 90, 170, 802]
print(radix_sort([1, 1000, 500, 10, 50]))              # [1, 10, 50, 500, 1000]
```

**Radix sort for strings (lexicographic):**

```python
def radix_sort_strings(words):
    """Sorts strings of equal length using LSD radix sort"""
    if not words:
        return words

    max_len = max(len(w) for w in words)
    # Pad shorter strings
    words = [w.ljust(max_len) for w in words]

    for pos in range(max_len - 1, -1, -1):   # Right to left
        # Stable sort by character at position `pos`
        words = sorted(words, key=lambda w: w[pos])

    return [w.strip() for w in words]


print(radix_sort_strings(["cat", "bat", "hat", "mat", "sat"]))
# ['bat', 'cat', 'hat', 'mat', 'sat']
```

**Key points:**
- Time complexity is O(d × n) where `d` is the number of digits. For fixed-width integers this is O(n).
- It is **stable** (since the inner counting sort is stable).
- It requires O(n + k) auxiliary space (k = size of alphabet/digit range).
- Typically used for integers, fixed-length strings, IP addresses, or dates.

---

## Part 4 — Python's Built-in Sorting

### Timsort — A Hybrid Algorithm

Python's `list.sort()` and `sorted()` use **Timsort**, invented by Tim Peters in 2002.

**Key idea:** Real-world data is rarely random — it often has partially-sorted subsequences ("runs"). Timsort exploits this:
1. Scan the array for natural runs (already ascending or descending sequences).
2. Extend short runs using **insertion sort** (which is O(n) on nearly-sorted data).
3. Merge adjacent runs using an optimized **merge sort**.

```python
# list.sort() — mutates the list in-place, returns None
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)   # [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() — returns a new list, original unchanged
original = [3, 1, 4, 1, 5, 9, 2, 6]
new_list = sorted(original)
print(original)  # [3, 1, 4, 1, 5, 9, 2, 6]  ← unchanged
print(new_list)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse order
print(sorted([3, 1, 4, 1, 5], reverse=True))  # [5, 4, 3, 1, 1]
```

---

### The `key` Function

The `key` parameter lets you specify a function that extracts a comparison value from each element.

```python
# Sort strings by length
words = ["banana", "fig", "apple", "kiwi", "cherry"]
print(sorted(words, key=len))
# ['fig', 'kiwi', 'apple', 'banana', 'cherry']

# Sort strings by last character
print(sorted(words, key=lambda w: w[-1]))
# ['banana', 'apple', 'fig', 'cherry', 'kiwi']

# Sort a list of tuples by the second element
students = [("Alice", 3.8), ("Bob", 3.5), ("Charlie", 3.9), ("Diana", 3.7)]
print(sorted(students, key=lambda s: s[1], reverse=True))
# [('Charlie', 3.9), ('Alice', 3.8), ('Diana', 3.7), ('Bob', 3.5)]

# Sort objects by attribute
class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price
    def __repr__(self):
        return f"{self.name}(${self.price})"

products = [Product("Hat", 25), Product("Shirt", 40), Product("Socks", 10)]
print(sorted(products, key=lambda p: p.price))
# [Socks($10), Hat($25), Shirt($40)]

# Using operator.attrgetter for cleaner attribute access
from operator import attrgetter
print(sorted(products, key=attrgetter("price")))
# Same result, often faster for large datasets
```

---

### Multi-key Sorting

```python
# Sort by grade (descending), then by name (ascending) on tie
students = [
    ("Alice", 90), ("Bob", 85), ("Charlie", 90),
    ("Diana", 85), ("Eve", 90)
]

# Tuple comparison: (-grade, name)
print(sorted(students, key=lambda s: (-s[1], s[0])))
# [('Alice', 90), ('Charlie', 90), ('Eve', 90), ('Bob', 85), ('Diana', 85)]

# Using itemgetter for multiple keys in the same direction
from operator import itemgetter
data = [("a", 3), ("b", 1), ("a", 1), ("b", 3)]
print(sorted(data, key=itemgetter(0, 1)))
# [('a', 1), ('a', 3), ('b', 1), ('b', 3)]
```

---

### The Decorate-Sort-Undecorate (DSU) Pattern

This is the design pattern underlying `key=`. It avoids calling the key function multiple times per comparison.

```python
# Manual DSU — equivalent to sorted(words, key=len)
words = ["banana", "fig", "apple", "kiwi", "cherry"]

# 1. Decorate: pair each element with its key
decorated = [(len(w), w) for w in words]
# [(6, 'banana'), (3, 'fig'), (5, 'apple'), (4, 'kiwi'), (6, 'cherry')]

# 2. Sort: Python sorts tuples lexicographically (key first, then element)
decorated.sort()
# [(3, 'fig'), (4, 'kiwi'), (5, 'apple'), (6, 'banana'), (6, 'cherry')]

# 3. Undecorate: strip the keys
result = [w for _, w in decorated]
print(result)  # ['fig', 'kiwi', 'apple', 'banana', 'cherry']


# Python's built-in key= does this automatically and efficiently:
print(sorted(words, key=len))  # Same output
```

**Why DSU matters for expensive keys:**

```python
import hashlib

words = ["banana", "fig", "apple", "kiwi", "cherry"] * 1000

# Without DSU: key function called O(n log n) times (at every comparison)
def expensive_key(w):
    return hashlib.sha256(w.encode()).hexdigest()

# With manual DSU: key function called exactly O(n) times
decorated = [(expensive_key(w), w) for w in words]   # n calls
decorated.sort()                                       # comparisons use precomputed keys
result = [w for _, w in decorated]
```

---

## Choosing the Right Algorithm

```
Is your data a list of integers in a fixed range?
  → Radix Sort or Bucket Sort (O(n))

Is n very small (< 20)?
  → Insertion Sort

Is the data nearly sorted?
  → Insertion Sort or Timsort (Python built-in)

Do you need stable sorting with guaranteed O(n log n)?
  → Merge Sort or Python's sorted()

Do you want in-place O(n log n) with no worst case risk?
  → Heap Sort

Do you want the fastest average case with in-place sorting?
  → Quick Sort (with random pivot)

Are you writing Python and want simplicity + performance?
  → Always use sorted() or list.sort() (Timsort is excellent)
```
