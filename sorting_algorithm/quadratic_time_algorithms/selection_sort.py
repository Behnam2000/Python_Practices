### Step-by-step trace on [29, 10, 14, 37, 13]:

# Step 1: unsorted = [29, 10, 14, 37, 13]  → min is 10 at index 1 → swap with index 0
#         → [10 | 29, 14, 37, 13]

# Step 2: unsorted = [29, 14, 37, 13]       → min is 13 at index 4 → swap with index 1
#         → [10, 13 | 29, 14, 37]

# Step 3: unsorted = [29, 14, 37]           → min is 14 at index 2 → swap with index 2
#         → [10, 13, 14 | 29, 37]

# Step 4: unsorted = [29, 37]               → min is 29, already in place
#         → [10, 13, 14, 29 | 37]

# Done:  [10, 13, 14, 29, 37]


## Implementation

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
print(selection_sort([29, 10, 14, 37, 13])) 
print(selection_sort([5, 5, 5, 5]))          # [5, 5, 5, 5] - only 4 swaps total


# ----------------
# Counting swaps:
# ----------------

def selection_swap_count(arr):
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
sorted_arr, swap_count = selection_swap_count(arr) 
print(f"sorted: {sorted_arr}, total swaps: {swap_count}")


# Key Points:
# _ Selection sort makes at most n-1 swaps - ideal when writes are expensive(e.g., flash memory)
# _ It always performs O(n²) comparisons, regardless of how sorted the input is.
# _ It is not stable by default - swapping can disrupt the order of equal elements.