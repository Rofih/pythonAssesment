'''
request for the first number
request for second number
request for third number
compare the numbers
display in increasing order
'''
first_number=int(input("enter first number:"))
second_number=int(input("enter second number:"))
third_number=int(input("enter third number:"))

if first_number>second_number and second_number>third_number:
	print(third_number,second_number,first_number)

if second_number>first_number and first_number>third_number:
	print(third_number,first_number,second_number)

if third_number>first_number and first_number>second_number:
	print(second_number,first_number,third_number)

if second_number>third_number and third_number>first_number:
	print(first_number,third_number,second_number)

if third_number>second_number and second_number>first_number:
	print(first_number,second_number,third_number)

if first_number>third_number and third_number>second_number:
	print(second_number,third_number,second_number)