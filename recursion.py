# Recursion : a function that calls itself from within
#             helps to visualize a complex problem in to basic steps , which can be solved more 
#             more easily iteratively or recursively.

# ITERATIVE:======================================================
def walk(steps) :
	for step in range(1 , steps + 1):
		print (f"you take step: {step}") # looping within a function
#walk(20)


def factorial(user_num):
	result = 1
	if user_num > 0:
		for y in range(1, user_num+1):
			#result = result * y
			result *= y
		return result	
		
		
print(factorial(6))


# RECURSIVE:===============================================================
def walk2(steps): 
	print (f"you take step: {steps}")

	walk2(steps - 1) # we're invoking this function from within. it's creating a loop but...
	#                 we will include the function it self whereas in ITERATION we're looping...
	#                 only within the function. 
#walk2(20)          # Begning at 20 and iterating downwards and going below zero
#                     (we need what is known as base condition. when do we want to STOP).

def walk3(steps):   # Add a Base condition:

	if steps == 0: # Base Condition/Case 
		return
	walk3(steps - 1)
	print(f"you take step: {steps}")

# walk3(20)


def factorial2(user_num):
	if user_num == 1:
		return 1
	else:
		return user_num * factorial2(user_num - 1)
		

print(factorial2(6))

