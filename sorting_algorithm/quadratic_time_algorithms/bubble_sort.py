### Step-by-step trace on [5, 3, 8, 1]:

# Pass 1:
#   [5, 3, 8, 1]  →  compare 5 & 3  → swap  → [3, 5, 8, 1]
#   [3, 5, 8, 1]  →  compare 5 & 8  → ok    → [3, 5, 8, 1]
#   [3, 5, 8, 1]  →  compare 8 & 1  → swap  → [3, 5, 1, 8]  ← 8 is now in place

# Pass 2:
#   [3, 5, 1, 8]  →  compare 3 & 5  → ok    → [3, 5, 1, 8]
#   [3, 5, 1, 8]  →  compare 5 & 1  → swap  → [3, 1, 5, 8]  ← 5 is now in place

# Pass 3:
#   [3, 1, 5, 8]  →  compare 3 & 1  → swap  → [1, 3, 5, 8]  ← done!


## Implementation:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: if no swaps happend, the list is already sorted
        if not swapped:
            break
    return arr

# Examples
print(bubble_sort([5, 3, 8, 1]))
print(bubble_sort([64, 34, 25, 12, 13, 22, 11, 90]))    
print(bubble_sort([1, 2, 3, 4, 5]))      #  [1, 2, 3, 4, 5] - only 1 pass needed
print(bubble_sort([5, 4, 3, 2, 1]))      # [1, 2, 3, 4, 5] - worst case


# Key Points:
# _ The "swapped" flag is an important optimization - if no swaps occurred in a full pass,
#       the array is sorted. This makes the best case O(n) for already-sorted data.
# _ Bubble sort is stable - equal elements are never swapped, so their relative order is preserved.
# _ Despite its simplicity, it is rarely used in practice becuase it performs O(n²) comparison even
#       when only a few elements are out of place.