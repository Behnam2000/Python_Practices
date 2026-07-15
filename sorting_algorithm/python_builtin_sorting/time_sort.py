# list-sort() - mutates the list in-place, returns None
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers) # [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() - returns a new list, original unchanged
original = [3, 1, 4, 1, 5, 9, 2, 6]
new_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5, 9, 2, 6]  ← unchanged
print(new_list)     # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse order
print(sorted([3, 1, 4, 1, 5], reverse=True))  # [5, 4, 3, 1, 1]