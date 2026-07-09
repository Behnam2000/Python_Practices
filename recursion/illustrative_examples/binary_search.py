def binary_search(data, target, low=0, high=None):
    if high is None:
        high = len(data) - 1

    if low > high:       # base case 1: target not found
        return -1
    
    mid = (low + high) // 2

    if data[mid] == target:    # base case 2: target found
        return mid
    
    elif data[mid] < target:     # target must be in the right half
        return binary_search(data, target, mid + 1, high)
    
    else:                        # target must be in the left half
        return binary_search(data, target, low, mid - 1)
    
data = [2, 5, 7, 10, 14, 19, 25, 31, 40]

print(binary_search(data, 14))

print(binary_search(data, 99))


## Trace for searching 19 in the list above (indices 0–8):

# Call 1: low=0, high=8, mid=4 → data[4]=14 < 19, go right
# Call 2: low=5, high=8, mid=6 → data[6]=25 > 19, go left
# Call 3: low=5, high=5, mid=5 → data[5]=19 == 19 ✓ return 5

# Only 3 calls to search 9 elements — this is O(log n) in action.