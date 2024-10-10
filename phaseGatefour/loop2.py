for count in range(1,7):
	print()
	for counter in range(1,count):
		if counter%2 == 0:
			print("*",end='')

		if counter%2 != 0:
			print(counter,end='')
for count in range(6,1,-1):
	for counter in range(1,count):
		if counter%2 != 0:
			print(counter,end='')

		if counter%2 == 0:
			print("*",end='')
	print()