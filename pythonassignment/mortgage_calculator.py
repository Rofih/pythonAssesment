'''
request user input
store as principal amount
request user input
store as annual interest rate
request user input
store as duration in years
state the constants
store the constants
display monthly mortgage payment
'''

principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = int(input("Enter the annual intrest rate: "))
duration_in_years = int(input("Enter the duration in years: "))

MONTHLY_IN_YEARS=12
PERCENTAGE_RATE=100


rate = (annual_interest_rate/100)/12
month = duration_in_years*12

monthly_payment1= rate*(1 + rate)**month
monthly_payment2=((1 + rate)**month)-1
monthly_mortgage_payment=principal_amount*(monthly_payment1/monthly_payment2)
print("The monthly mortgage payment is$ ",(round(monthly_mortgage_payment,2)))

