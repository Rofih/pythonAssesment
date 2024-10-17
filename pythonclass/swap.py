def swapper(number):
	for count in range(1,len(number)-1,2):
		temp = number[count]
		number[count] = number[count-1] 
		number[count-1] = temp
	return number