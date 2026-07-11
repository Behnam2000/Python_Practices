##  Partition example with pivot = 10 on [3, 6, 8, 10, 1, 2, 1]:

# Pivot: 10
# Less than 10:    [3, 6, 8, 1, 2, 1]
# Equal to 10:     [10]
# Greater than 10: []
# → [3, 6, 8, 1, 2, 1] + [10] + []
# Recurse on left...


## Implementation(clean functional style):

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]   # choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))  # [1, 1, 2, 3, 6, 8, 10]



### Lomato partiton scheme:

# The Lomuto scheme traditionally chooses the last element of the array as the pivot. 
#   It then uses two "pointers" (usually index variables i and j) to scan and arrange the data.

# 1 → The Pivot: Select the last element.

# 2 →  Pointer i (The Boundary): This pointer keeps track of the boundary where elements smaller than the pivot end. 
#       It starts at one position before the first element (low - 1).

# 3 → Pointer j (The Explorer): This pointer scans through the array from the first
#       element up to the element just before the pivot.

# 4 → The Comparison: As j scans, it compares the current element to the pivot.

#           - If the element is smaller than or equal to the pivot, we increment i by 1, and swap the elements at i and j.

#           - If the element is greater than the pivot, j simply moves on.

# 5 → The Final Swap: Once j finishes scanning, the pivot is swapped with the element at i + 1.
#        This safely lands the pivot exactly in its correct sorted position.

## Implementation (in-place with Lomuto partition scheme):

def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition the array and get the pivot index
        pivot_idx = partition(arr, low, high)

        # Recursively sort the elements before and after partition
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)
    return arr

def partition(arr, low, high):
    # 1. Choose the last element as the pivot:
    pivot = arr[high]  

    # 2. i tracks the boundary of smaller elements
    i = low - 1

    # 3 & 4. j scans the array
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 # Move the boundary forward

            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    # 5. Place the pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the final index of the pivot
    return i + 1

arr = [10, 7, 3, 9, 1, 2, 5]
print(quick_sort_inplace(arr))



## The worst case problem and how to avoid it:

# Worst case: sorted or reverse-sorted input with a naive pivot choice
# [1, 2, 3, 4, 5] with pivot=first element → O(n²)

# Fix 1: Random pivot
import random
def quick_sort_random(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]  # Swap random with last
        pivot_idx = partition(arr, low, high)
        quick_sort_random(arr, low, pivot_idx - 1)
        quick_sort_random(arr, pivot_idx + 1, high)

        return arr

# Fix 2: Median-of-three pivot

# The Median-of-Three strategy fixes this by sampling a small cross-section of the array before partitioning:

# 1 → Sample: Look at exactly three elements: the first, the middle, and the last.

# 2 → Sort the Sample: Sort just those three elements among themselves so the smallest is at the start,
#       the largest is at the end, and the median is in the middle.

# 3 → Position the Pivot: Take that median value and swap it to the end of the array (or just before the end)
#       so it can act as the pivot for your standard partition logic.

def median_of_three(arr, low, high):
    mid = (low + high) // 2

    # Sort low, mid, high, and pick middle as pivot

    # 1 & 2. Sort the elements at low, mid, and high
    # We do this using three simple comparisons and swaps
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low] 
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    # Place pivot at high-1

    # 3. The median is now sitting at the 'mid' index.
    # Swap it with the 'high' index so Lomuto can use it as the pivot.
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]

    return arr[high - 1]


def lumato_partition_optimized(arr, low, high):
    # Optimize pivot selection before partitioning
    median_of_three(arr, low, high)

    # Now arr[high] holds our safe median pivot
    # The rest of this is identical to standard Lomato
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= arr[i]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test:
my_arr = [80, 20, 10, 40, 70, 90, 30, 50]
op_lomato = lumato_partition_optimized(my_arr, 0, len(my_arr) - 1)





# Key Points:

# _ Average case O(n log n), but O(n²) in the worst case (nearly sorted data with bad pivot).
# _ In practice, it is often faster than Merge Sort due to better cache performance.
# _ It is not stable in its standard form.
# _ It can be implemented in-place using O(log n) stack space for recursion.