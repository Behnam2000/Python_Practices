# Sort by grade (desending), then by name (acending) on tie
students = [
    ("Alice", 90), ("Bob", 85), ("Charlie", 90),
    ("Diana", 85), ("Eve", 90)
]

# Tuple comparison: (-grade, name)
print(sorted(students, key=lambda s: (-s[1], s[0])))
# [('Alice', 90), ('Charlie', 90), ('Eve', 90), ('Bob', 85), ('Diana', 85)]


# Using itemgetter for multiple keys in the same direction
from operator import itemgetter
data = [("a", 3), ("b", 1), ("a", 1), ("b", 3)]
print(sorted(data, key=itemgetter(0, 1)))
# [('a', 1), ('a', 3), ('b', 1), ('b', 3)]