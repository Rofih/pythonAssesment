cost_of_car=float(input("enter cost of car:"))

if cost_of_car > 10000000 :
	print(0.20*cost_of_car)

elif cost_of_car > 5000000 and cost_of_car < 10000000:
	print(0.15*cost_of_car)

elif cost_of_car > 2500000 and cost_of_car < 5000000:
	print(0.10*cost_of_car)

elif cost_of_car < 2500000:
	print(0.05*cost_of_car)
