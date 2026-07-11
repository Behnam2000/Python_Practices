## Understanding a Max-Heap:

# Array: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

# As a tree:
#            16
#          /    \
#        14      10
#       /  \    /  \
#      8    7  9    3
#     / \  /
#    2   4 1

# Parent of index i → index (i-1)//2
# Left child of i  → 2i + 1
# Right child of i → 2i + 2

## Implementation

def heapify(arr, n, i):
    """
    Maintain the max-heap property for subtree rooted at index i.
    n = current heap size (elements beyond n are sorted)
    """

    largest = i         # Assume root is largest
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursively fix the affected subtree

def heap_sort(arr):
    n = len(arr)

    # Phase 1: Build max-heap (starts from last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Phase 2: Extract elements one by one:
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Move max to end
        heapify(arr, i, 0)      # Restore heap for remaining elements

    return arr

print(heap_sort([12, 11, 13, 5, 6, 7]))   # [5, 6, 7, 11, 12, 13]
print(heap_sort([1]))                       # [1]
print(heap_sort([3, 1, 4, 1, 5, 9, 2, 6])) # [1, 1, 2, 3, 4, 5, 6, 9]



## Using Python's heapq (min-heap):

import heapq

def heap_sort_builtin(arr):
    heapq.heapify(arr)   # O(n) build
    return [heapq.heappop(arr) for _ in range(len(arr))]      # O(n log n) extract

print(heap_sort_builtin([3, 1, 4, 1, 5, 9, 2, 6]))  # [1, 1, 2, 3, 4, 5, 6, 9]


# Key Points

# Avarage case O(n log n), but O(n²) in the worst case (nearly sorted data with bad pivot).
# In practice, it is often faster than Merge Sort due to better cache performance.
# It is not stable in its standard form.
# It can be implemented in-place using O(log n) stack space for recursion.
