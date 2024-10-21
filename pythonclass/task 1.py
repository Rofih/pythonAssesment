'''
request for  deposit

request for withdrawal amount


'''
deposit=int(input("Enter amount:"))
while deposit>0:
	deposit=int(input("Enter an amount:"))
        
	print(deposit)
	user_input=int(input("Enter amount:"))
	withdraw_amount=deposit-user_input
	print(withdraw_amount)