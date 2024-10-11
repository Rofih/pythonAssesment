import random
value = []
number=input("enter a number:")
value = number.split(',')



number2=random.randrange(50)
number3=random.randrange(50)
number4=random.randrange(50)

array = [number2,number3,number4]

if array[0]==value[0] and array[1]==value[1] and array[2]==value[2]:
	print("you won $5000")


elif array[0]==value[0] or array[0]==value[1] or array[0]==value[2] and array[1]==value[0] or array[1]==value[1] or array[1]==value[2] and array[2]==value[0] or array[2]==value[1] or array[2]==value[2]:
	print("you won $4000")


elif array[0]==value[0] or array[1]==value[1] or array[2]==value[2]:
	print("you won $3000")
else:
	print("mr sk i don chop your money")



