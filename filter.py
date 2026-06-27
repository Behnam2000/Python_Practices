alist = [1,2,3,4,5,6,7,8,9]

#
def over_three(user_list):
	over_three_list = []
	for num in user_list:
		if num > 3 :
			over_three_list.append(num)
	return over_three_list

print(over_three(alist))
#

#
def over_two(li_1):
	li_2 = [x for x in li_1 if x>2]
	return li_2
print (over_two(alist))
#


#
print(list(filter(lambda x: x > 4 , alist)))
#

def over_five(x):
	if x <= 5:
		return False
	else:
		return True
over_5 = filter(over_five , alist)
print(over_5)
for x in over_5:
	print(x)

n = [4,3,2,1]
print("Square Using tha Filter function don't work (it acceptes bool): " ,list(filter(lambda x:x**2 , n)))z