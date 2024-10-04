'''
when number is inputed break it down to digits
then reverse
use the reverse and confirm with the number 
'''
def reverse(number):
	reverse = 0
	add = 0
	while number!=0:
		remainder = number%10
		reverse = (reverse *10) + remainder
		number = number//10
		
	return reverse

def is_palindrome(number):
	if reverse(number)==number:
		return True
	else:
		return False