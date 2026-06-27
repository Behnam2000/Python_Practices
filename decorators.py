import humanize

scores = 1000345

def human(nums):
	def myInner(x):
		number = nums(x)
		return humanize.intcomma(number)
	return myInner	



@human
def avarage(parts):
	power = parts * 10
	return power
	


print(avarage(12334))