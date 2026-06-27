person = 26, 520.34, 'Behnam', True

for i in person:
	print(f"Value: {i} Type: {type(i)}")

	add = person[0] + person[1]

print (add)

print("\n")

age = 25               # int
price = 9.99           # float
name = "Alice"         # str
is_active = True       # bool

print(age, type(age))
print(price, type(price))
print(name, type(name))
print(is_active, type(is_active))

print(f"Sum of int + float: {age + price}")