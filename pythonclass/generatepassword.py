import random
import string
def get_password():
	value = string.printable
	array = [value]
	lst = []
	password = " "
	for count in range(16):
		number = random.choice(value)
		lst.append(number)
	
	password = ''.join(lst) 
	return password


print(get_password())