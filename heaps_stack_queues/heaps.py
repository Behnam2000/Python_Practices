import heapq

min_heap = []

# Push elements (Notice they won't necessarily stay in standard sorted order, 
# but the smallest will always be at index 0)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 2)
print(f"Heap array: {min_heap}")       # [2, 4, 15, 10]

# Pop the smallest element
smallest = heapq.heappop(min_heap)
print(f"Popped smallest: {smallest}")  # 2
print(f"Heap after pop: {min_heap}")   # [4, 10, 15]

# To convert an existing list into a heap in-place in O(n) time:
nums = [5, 1, 9, 3]
heapq.heapify(nums)
print(f"Heapified list: {nums}")       # [1, 3, 9, 5]


## A Note on Max-Heaps: Python's heapq only supports min-heaps.
# The standard Pythonic workaround for creating a max-heap is to
# multiply your numeric values by -1 before pushing them,
# and then multiply by -1 again when you pop them out.