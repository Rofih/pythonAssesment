user_input=int(input("Enter the number:"))
user_input1=user_input+1

space=" "

for count in range(1,user_input1):
	for counter in range(count,1,-1):
		print(space*count,counter,end=" ")
		counter-=1



	for value in range(1,count+1):
		print(space*count,value,end=" ")

		



