'''
declare a list
request for number
store as number
display list
add number requested
calculate amount of element
divide addition and amount
store as avg
display avg
'''
count=int(input("to stop enter0:"))
counter=0
number=0
numberlist=[]
while count != 0:
	count=int(input("enter number:"))
	number+=count
	#numberlist+=count
	if count==0:
		break
	numberlist.append[count]
print(numberlist)
avg=counter/len(numberlist)
print(avg)