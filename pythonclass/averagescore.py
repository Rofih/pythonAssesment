'''
request for student score
count number of scores
sum scores
divide the sum to the nummber of scores
display the result

'''
count=0
score=0
user_input=0
loop=0
while loop<2:
	user_input=int(input("Enter students score:"))
	count+=1
	user_input+=score
	loop+=1
print(score/count)