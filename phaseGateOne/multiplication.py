def multiply(number,value):
	add=0
	if number<0:
		for counter in range(value):
			add+=number
		return add
	else:
		for count in range(number):
			add+=value
		return add