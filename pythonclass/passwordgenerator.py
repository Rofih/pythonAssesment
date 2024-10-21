import random
def get_password():
	array = [[string.ascii_letters],[string.digits],[string.punctuation],[string.printable]]
	lst = []

	for count in range(16):
		number = random.randrange(30)
		value = random.randrange(35)
		lst[count] = array[number][value] 
	return lst