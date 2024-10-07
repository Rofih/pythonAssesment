'''
request for user input
compare for each input
display the price
'''
user_input=float(input("enter a number of units used:"))

removal = user_input -100
price = 0
price_for_100_units = 100 * 50

if user_input < 0:
	print("invalid input")


if removal >100:
	removal2 = removal - 100
	price = 100 * removal2
	sum = price_for_100_units + price
	print("#",sum)
else:
	price = 50 * removal
	print("#",price)
