'''
request for user input then store
generate a random number then store
generate another random number then store
sum the the generated random numbers
'''
import random
user_input = int(input("enter the sum of the random generated numbers:"))

number = random.randrange(100)
number2 = random.randrange(100)

add = number+number2

if user_input == add:
	print("true")
else:
	print("false")