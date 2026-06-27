from functools import reduce

num = [2,3,4,5,6,7,8,9,10]
num2 = [100,2,4,2,1] 
num3 = [5,4,3,2,1]
# Normal function doing as such as reduce() 
def mult(li1):
	prod = li1[0]
	for i in range(1,len(li1)):
		prod *= li1[i]
	return prod
	
print(mult(num3))		

# reduce : (first item * second item)=result1 => (result1 * third item)= result2 and so on... 

#reduce 
print(reduce(lambda x , y: x / y, num2))
#   100 / 2 = 50
#   50 / 4 = 12.5
# 12.5 / 2 = 6.25
# 6.25 / 1 = 6.25


def add(x , y):
    return x + y

print(reduce(add , num3 , 8))


# How reduce function in functools lib is working:


initial_missing = object()

def reduce(function, iterable, initial=initial_missing, /):
    it = iter(iterable)
    if initial is initial_missing:
        value = next(it)
    else:
        value = initial
    for element in it:
        value = function(value, element)
    return value

print(reduce(add, num))    