amount=int(input("Enter principal amount: "))
rate=int(input("Enter the annual intrest rate: "))
duration=int(input("Enter the duration in years: "))

rate1=rate/100
duration1=duration/12

value1=int(rate1*(1+rate1)^duration1)
value2=int(((1+rate1)^duration1)-1)
mortgage=int(amount*(value1/value2))
print("Your monthly payment is ",mortgage)