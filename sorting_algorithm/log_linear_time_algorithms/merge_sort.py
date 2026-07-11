## Visualization of the divide & merge :

#            [38, 27, 43, 3, 9, 82, 10]
#            /                       \
#     [38, 27, 43, 3]           [9, 82, 10]
#       /          \               /      \
#   [38, 27]    [43, 3]       [9, 82]    [10]
#    /    \      /    \        /    \
#  [38]  [27]  [43]  [3]    [9]  [82]
#    \    /      \    /        \    /
#   [27, 38]   [3, 43]       [9, 82]
#        \          /               \
#     [3, 27, 38, 43]            [9, 10, 82]
#               \                    /
#             [3, 9, 10, 27, 38, 43, 82]


## Implementation:

def merge_sort(arr) -> object:
    # Base case : a list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (Merge)
    return merge(left, right)

def merge(left, right) -> list:
    result = []
    i = j = 0

    # Compare the front of each sorted half and take the smaller
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If any elements are left over in either array, add them
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Examples
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([1]))                           # [1]
print(merge_sort([]))                            # []
print(merge_sort(["enzo", "camaro", "audi", "honda", "mercedes", "yamaha", "bmw", "quatro", "scania"]))



## Tracing the merge step:

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
    
verbose = merge_verbose([3, 27, 38, 43], [9, 10, 82])
# Comparing 3 vs 9   → take 3
# Comparing 27 vs 9  → take 9
# Comparing 27 vs 10 → take 10
# Comparing 27 vs 82 → take 27
# Comparing 38 vs 82 → take 38
# Comparing 43 vs 82 → take 43
# Remaining [82] appended
print(verbose)



# Key Points:

# _ Guaranteed O(n log n) in all cases — no worst case degradation.
# _ The downside is O(n) extra memory needed for the merged temporary arrays.
# _ It's stable
# _ prefereed when stability is required, or when sorting linked lists (no random access needed)