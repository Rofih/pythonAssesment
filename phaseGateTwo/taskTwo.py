value1=0
value2=0
value3=0
value4=0
for count in range(1000,3000):
	if count>=2000 and count<=3000:
		value1=count%10
		value2=count//10
		value3=value2%10
		value4=value2//10
		if value1%2==0 and value2%2==0 and value3%2==0 and value4%2==0:
				print(count,end=",")