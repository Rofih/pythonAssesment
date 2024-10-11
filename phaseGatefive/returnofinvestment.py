investment_amount = float(input("Enter investment amount:"))

no_of_years = int(input("Enter number of years:"))

percentage = float(input("Enter percentage:"))

	 



print("year     ROI        amountas")
for count in range(no_of_years):
	if investment_amount < 0 or no_of_years < 0 or percentage < 0:
		print("invalid input,olay")
	break
	intrest = (investment_amount//100)*percentage

	investment_amount = investment_amount + intrest
	 
	print(f'{count}     {intrest:,}     {investment_amount:,}')
	

