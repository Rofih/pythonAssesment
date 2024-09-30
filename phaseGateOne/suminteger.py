user_input=int(input("enter the integer:"))
if user_input>00 and user_input<100:
	digit=user_input%10
	number=user_input//10
	digit2=number%10
	add=digit+digit2
	print("the sum is",add)
if user_input>100 and user_input<1000:
	digit=user_input%10
	number=user_input//10
	digit2=number%10
	digit3=number//10
	sum=digit+digit2+digit3
	print("the sum is",sum)
	