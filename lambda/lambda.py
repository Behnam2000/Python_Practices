even_or_odd = lambda x: 'Even' if x % 2 == 0  else "Odd"
print(even_or_odd(13))


myTuple = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
myTuple.sort(key= lambda x: x[1])
print(myTuple)


# lambda conditionals:
mx = lambda x , y: x if x > y else y
print(mx(7,6))

starts_with_j = lambda x: True if x.startswith('J') else False
print(starts_with_j('Joey'))

wordb4 = lambda s , w : s.split()[s.split().index(w)-1] if w in s else None
sentence =  "Four score and seven years ago"
print(wordb4(sentence , 'years'))

def doing(f , val):
	return f(val)
	
func = lambda x: x**3
print(func(16))
print(doing(func , 2))

