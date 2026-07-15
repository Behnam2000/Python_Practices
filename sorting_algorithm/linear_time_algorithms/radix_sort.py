# Step-by-step example on [170, 45, 75, 90, 802, 24, 2, 66]:

# Original:   [170, 45, 75, 90, 802, 24, 2, 66]

# Pass 1 (ones digit):
#   Digits:      0,   5,  5,  0,   2,  4, 2,  6
#   Buckets:  0:[170,90]  2:[802,2]  4:[24]  5:[45,75]  6:[66]
#   After:    [170, 90, 802, 2, 24, 45, 75, 66]

# Pass 2 (tens digit):
#   Digits:      7,  9,  0,  0,  2,  4,  7,  6
#   Buckets:  0:[802,2]  2:[24]  4:[45]  6:[66]  7:[170,75]  9:[90]
#   After:    [802, 2, 24, 45, 66, 170, 75, 90]

# Pass 3 (hundreds digit):
#   Digits:      8,  0,  0,  0,  0,  1,  0,  0
#   Buckets:  0:[2,24,45,66,75,90]  1:[170]  8:[802]
#   After:    [2, 24, 45, 66, 75, 90, 170, 802]  ← SORTED!


## Implementation

def counting_sort_by_digit(arr, exp):
    """Stable sort of arr by the digit at position exp (1, 10, 100, ...)"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9

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




## Radix sort for strings (lexicographical)
def radix_sort_strings(words):
    """Sorts strings of equal length using LSD radix sort"""
    if not words:
        return words
    
    max_len = max(len(w) for w in words)

    # Pad shorter strings
    words = [w.ljust(max_len) for w in words]

    for pos in range(max_len - 1, -1, -1):  # Right to left
        # Stable sort by character at position 'pos'
        words = sorted(words, key=lambda w: w[pos])

    return [w.strip() for w in words]

print(radix_sort_strings(["cat", "bat", "mat", "hat", "sat"]))



# Key points:

# -  Time complexity is O(d × n) where d is the number of digits. For fixed-width integers this is O(n).
# -  It is stable (since the inner counting sort is stable).
# -  It requires O(n + k) auxiliary space (k = size of alphabet/digit range).
# -  Typically used for integers, fixed-length strings, IP addresses, or dates.
