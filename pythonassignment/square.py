import math
def divide_or_square(number):
	if number < 0:
		raise ValueError("invalid number")
	if number%2==0:
		return math.sqrt(number)
	else:
		return number/5