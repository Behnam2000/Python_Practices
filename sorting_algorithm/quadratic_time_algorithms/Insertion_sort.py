### Step-by-step trace on [4, 3, 2, 10, 12, 1, 5, 6]:

# Start:       [4 | 3, 2, 10, 12, 1, 5, 6]
# Insert 3:    [3, 4 | 2, 10, 12, 1, 5, 6]   (shift 4 right)
# Insert 2:    [2, 3, 4 | 10, 12, 1, 5, 6]   (shift 4, 3 right)
# Insert 10:   [2, 3, 4, 10 | 12, 1, 5, 6]   (already in place)
# Insert 12:   [2, 3, 4, 10, 12 | 1, 5, 6]   (already in place)
# Insert 1:    [1, 2, 3, 4, 10, 12 | 5, 6]   (shift everything right)
# Insert 5:    [1, 2, 3, 4, 5, 10, 12 | 6]
# Insert 6:    [1, 2, 3, 4, 5, 6, 10, 12]


## Implementation:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]           # the element to be inserted
        j = i -1
        # Shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Examples
print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))  # [1, 2, 3, 4, 5, 6, 10, 12]
print(insertion_sort([1, 2, 3, 4, 5]))              # O(n) - already sorted, no shifts!
print(insertion_sort(["banana", "apple", "cherry"]))  # ['apple', 'banana', 'cherry]



# -------------------------------------
# Why it shines on nearly-sorted data:
# -------------------------------------
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
print(f"Reversed: {time_sort(insertion_sort, random_data):.6f}s")


# Key Points:

# _ Best case is O(n) when data is already sorted - no inner loop iterations occur.
# _ It is stable and in-place.
# _ It is the algorithm for choice for small arrays and is used internally by Timesort(Python built-in)
#       for small sub-sequences.