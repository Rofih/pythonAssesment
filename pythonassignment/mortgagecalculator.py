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

MONTH_IN_YEAR = 12
PERCENTAGE_RATE = 100


percentage_monthly_rate = (annual_interest_rate/100)/12
duration_In_months = duration_in_years*12

monthly_mortgage_payment = principal_amount*((calculated_rate*(1 + calculated_rate)**duration_In_months)/((1 + calculated_rate)**duration_In_months)-1)

print("The monthly mortgage payment is$ ",(round(monthly_mortgage_payment,2)))

