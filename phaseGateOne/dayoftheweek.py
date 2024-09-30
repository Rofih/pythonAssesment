'''
request for today
request for number of days elapsed
display the day and the future day
'''

sunday = 0
monday = 1
tuesday=2
wednesday=3
thursday=4
friday=5
saturday=6


Sunday ="sunday"
Monday = "monday"
Tuesday="tuesday"
Wednesday="wednesday"
Thursday="thursday"
Friday="friday"
Saturday="satuday"


day=int(input("enter today's day:"))
elapsed_day=int(input("enter the numbers of days elapsed since today:"))
add=day+elapsed_day
if add==0 or add==7:
	print("the future day is",Sunday)
if add==1 or add==8:
	print("the future day is",Monday)
if add==2 or add==9:
	print("the future day is",Tuesday)
if add==3 or add==10 :
	print("the future day is",Wednesday)
if add==4 or add==11:
	print("the future day is",Thursday)
if add==5 or add==12:
	print("the future day is",Friday)
if add==6 or add==13:
	print("the future day is",Saturday)





