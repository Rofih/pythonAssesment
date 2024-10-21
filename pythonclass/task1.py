'''
request for  deposit
request for wanted withdrawal amount
display withdrawal amount

'''
deposit=int(input("Enter amount:"))
amount=0
while deposit>0:
	deposit=int(input("Enter an amount:"))
	amount+=deposit  
	print(amount)
	user_input=int(input("Enter amount you want to withdraw:"))
	if deposit>amount:
		print(amount)
	else:
		print("your balance is not sufficient")
	balance_amount=amount-user_input
	print("Your balance is",balance_amount) 