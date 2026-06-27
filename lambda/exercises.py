# Exercise 1:
multiplier = lambda a, b: a * b 
print(multiplier(5, 6))

# Exercise 2:
cel_to_f = lambda c: f"{c} Celsius is: {(c * 1.8) + 32} Fahrenheit"
print(cel_to_f(0))
print(cel_to_f(100))

# Exercise 3
words = ["apple", "banana", "cherry", "date", "fig"]
filter_words = list(filter(lambda x: len(x) > 4, words))
print(filter_words)

# grab the last letter of a string using negative indexing
sorted_words = sorted(words, key=lambda x: x[-1])
print(sorted_words)