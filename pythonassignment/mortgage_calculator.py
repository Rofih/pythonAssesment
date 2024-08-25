amount=int(input("Enter principal amount: "))
rate=int(input("Enter the annual intrest rate: "))
duration=int(input("Enter the duration in years: "))


value1=int(rate*(1+rate)^duration)
value2=int(((1+rate)^duration)-1)
mortgage=int(amount*(value1/value2))
print("Your monthly payment is ",mortgage)