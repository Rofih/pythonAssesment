'''
request for user input 
compare for divisibility
display whether or not divisible
'''
'''
request for user input
compare if is a multiple
display result
'''

user_input=float(input("enter a number:"))
if user_input < 0 :
	print("invalid input")

if user_input% 7==0:
	print("it is divisible")
else:
	print("it is not divisible")

number=int(input("enter a number2:"))
if number < 0 :
	print("invalid input")

if number% 3 ==0:
	print("bye")