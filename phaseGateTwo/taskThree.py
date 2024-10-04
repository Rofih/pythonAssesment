number_list=[1,2,3,4,5,6,7,8,9,11]
length=0
add = 0
add_even=0
add
for count in number_list:
	length+=1
	add+=number_list[count]
	if count%2==0:
		add_even+=number_list[count]
print(length)
print(add)
print(add_even)
average = add / length
print(average)
	