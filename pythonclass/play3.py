def add_number(value):
	
	if(value >= 1andvalue <= 999):
		if(value >= 10andvalue <= 99):
			if(value%2==0):
				digit = input%10
				digit1 = input/10
				digit3 = digit+digit1
				return digit3
			elif(value%2>=1):
				digit = input%10
				digit1 = input/10
				digit3 = digit-digit1
				return digit3

		else
			if(value%2==0)
				digit = input%10
				digit2 = input/10
				digit3 = digit2%10
				digit4 = digit2/10
				return digit+digit3+digit4
			if(value%2>=1)
				digit = input%10
				digit2 = input/10
				digit3 = digit2%10
				digit4 = digit2/10
				return digit-digit3-digit4

	
print(add_number(77))