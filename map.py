def factorial(number):
	if number == 1:
		return 1
	else:
		return number * factorial(number - 1)

# user = int(input("Enter a Number: "))
#print(f"{user} factorial = {factorial(user)}\n")

myNumList = [1,2,3,4,5,6,7]
print(list(map(factorial , myNumList)))

#===================== Square Numbers in a list
#Standard python function:
def square(List_1):
	List_2 = []

	for num in List_1:
		List_2.append(num ** 2)
	return List_2	

print(f"\nSquare With Standard python function: {square([4,3,2,1])}")

#Using tha Map function (lambda):
n = [4,3,2,1]
print("Square Using tha Map function: " , list(map(lambda x:x**2, n)))