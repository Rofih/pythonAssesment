import random
subtract = 0
won = 0
fail = 0
for count in range(10):
	number = random.randrange(50)
	number2 = random.randrange(50)

	if number2 > number:
		subtract = number2 - number
		print(f'what is {number2} - {number}')
	else:
		subtract = number - number2
		print(f'what is {number} - {number2}')
	
	user_input = int(input('enter your answer:'))

	if user_input == subtract:
		print("correct")
		won += 1
	else:
		print("incorrect")
		fail += 1
print("your final score is",won)