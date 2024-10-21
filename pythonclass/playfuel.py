'''
display conversion
request for budget 

display price per litre
display price
'''
'''
print("1liter=$855")
budget=float(input("Enter amount budgeted:"))
if budget>855:
	liter=budget/855
	print("you can buy this amount of fuel",liter)
	print("the price is",liter*855)
if budget<855:
	liter=budget/855
	print("you can buy this amount of fuel",liter)
	print("the price is",liter*855)

'''
'''
request for celsius
store as celsius
convert to fahrenheit
'''
'''
celsius=float(input("Enter the celsius degreee:"))
fahrenheit=(9/5)*celsius+32
print(fahrenheit)
'''

import time
clock=time.time()
minute=(clock%60)/60
hour=clock/60
sec=clock%60
sec2=sec/60
sec3=sec2/60
print(hour,minute,sec)

'''
import datetime
time=datetime.datetime.now()
print(time)
'''