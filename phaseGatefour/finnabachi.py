user_input = int(input("enter a number:"))
array = []
display = []
for count in range(user_input):
	sum = count + (count+1)
	array = [count,(count+1),sum]
	for countee in range(3):
		display[count] = array[countee]
		print(display[count])