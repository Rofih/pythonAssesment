def sumString(number,number2):
	if str(number)!= number and str(number2)!= number2:
		raise TypeError("invalid input")
	convert_to_float = float(number)
	convert2_to_float = float(number2)
	sum = convert_to_float + convert2_to_float
	to_string=str(sum)
	return to_string