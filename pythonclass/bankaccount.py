'''
request for deposit
store deposit
request for withdrawal
display amount
'''
while True:
	list='''
	1-to deposit enter 1.
	2-to withdraw enter 2.
	'''
	print(list)
	amount=0
	user_input=int(input("Enter your option:"))

	match (user_input):
		case 1:
			deposit=float(input("Enter amount:"))
			amount+=deposit
		case 2:
			withdraw=int(input("Enter amount you want to withdraw:"))
			if deposit < withdraw:
				print("insufficient fund")
			if deposit > withdraw:
				balance=amount-withdraw
				print(balance)

	