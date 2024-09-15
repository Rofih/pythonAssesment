def future_investment(investment_amount,monthly_interestRate,years):
	if investment_amount<=0 and monthly_interestRate<=0 and years<=0:
		raise ValueError("invalid input")
	MONTHS_IN_A_YEAR=12
	numberOfMonths=years/12
	return investment_amount*(1+monthly_interestRate)**numberOfMonths