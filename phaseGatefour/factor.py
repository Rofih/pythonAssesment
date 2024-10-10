def factorial(number):
	value = []
	for count in range(number):
		value[count]= number*(count+1)
	return value
print(factorial(10))



def vowel_checker(character):
	if character == "a" or character == 'e' or character == "i" or character == "o" or character == "u":
		return True
	else:
		return False
print(vowel_checker("z"))