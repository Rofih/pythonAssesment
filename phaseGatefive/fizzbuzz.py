for count in range(1,51):
	if count % 5 == 0 and count % 3 == 0:
		print("fizzbuzz")
	elif count%5==0:
		print("buzz")
	
	elif count%3==0:
		print("fizz")
	else:
		print(count)
