'''
request for name
store it as name
if user enters a name display hello name
if user does not display invalid name

'''


name=(input("Enter your name:  "))

if name=="":
	print("invalid name")

if name!="":
	print("Hello",name)
