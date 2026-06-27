print("\n \t \t ======= Interger zipping \n ")
list_a = [1, 2, 2, 5, 9, 9, 9, 14]
list_b = [2, 3, 9, 9, 20]

print("\t list format: " , list(zip(list_a , list_b)))
print("\n \t dict format: " , dict(zip(list_a , list_b)))
print("\n \t set format: " , set(zip(list_a , list_b)))
print("\n \t tuple format: " , tuple(zip(list_a , list_b)))


print("\n \t \t========== String zipping \n ")
list_str_a = ["Behnam", "Alireza", "Amir", "Shayan", "Bahar", "Reza", "Mohammad"]
list_str_b = ["Benz", "Chevy", "Biuck", "Chery", "Perado"]

print("\t list format: " , list(zip(list_str_a , list_str_b)))
print("\n \t dict format: " , dict(zip(list_str_a , list_str_b)))
print("\n \t set format: " , set(zip(list_a , list_b)))
print("\n \t tuple format: " , tuple(zip(list_a , list_b)))


print("\n \t \t ========== Mixed Zipping \n ")
list_mixed_a = [1, 2.5, "apple", True, None, (3, 4), {"k": 5}, [6, 7], {8, 9}, b"bytes"]
list_mixed_b = [2.5, "banana", False, None, (3, 4), {"k": 5}, [6, 7, 8], frozenset({9, 10}), 1+2j, b"bytes"]


print("\t" , list(zip(list_mixed_a , list_mixed_b)))
