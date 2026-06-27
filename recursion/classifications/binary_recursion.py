# Example 1 ---- Summing a sequence by splitting in half
def binary_sum(data, start, stop):
    """Divide the sequence in half , sum each halp recursively"""

    if start >= stop:           # base case: empty slice
        return 0
    
    if start == stop - 1:       # base case: single element
        return data[start]
    
    mid = (start + stop) // 2
    left = binary_sum(data, start, mid)  # recursive call 1
    right = binary_sum(data, mid, stop)  # recursive call 2
    return left + right

data = [1, 2, 3, 4, 5, 6, 7, 8]

print(binary_sum(data, 0, len(data)))

# Example 2 ---- Drawing an English ruler (the classic textbook example)
def draw_line(length, label=""):
    print(f"-" * length + (" " + label if label else ""))

def draw_interval(center_length):
    """Draw the tick marks between two major ticks"""

    if center_length > 0:
        draw_interval(center_length - 1)  # upper half
        draw_line(center_length)
        draw_interval(center_length - 1)  # lower half (two calls !)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, "0")
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

draw_ruler(2, 3)

# Binary recursion has O(log n) depth but can produce O(n) total work overall (e.g., merge sort is O(n log n)).