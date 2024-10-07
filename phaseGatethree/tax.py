filing_status = '''
0->Single filers.
1->Married filing jointly.
2->Married filing separately.
3->Head of household.
'''
print(filing_status)

user_input = int(input("enter filing status:"))
taxable_income = float(input("enter taxable income:"))
tax = 0
total_tax = 0
if user_input == 0:
	#taxable_income = taxable_income - 8350
	

	if taxable_income > 0 and taxable_income < 8350:
		tax = taxable_income * 0.10
		print("your tax is",tax)

	elif taxable_income > 8351 and taxable_income < 33950:
		tax_for_10_percent = 8350 * 0.10
		taxable_income = taxable_income - 8350
		tax = taxable_income * 0.15
		total_tax =  tax_for_10_percent  + tax
		print("your tax is",total_tax)

	elif taxable_income > 33951 and taxable_income < 82250:
		taxable_income = taxable_income - 8350
		taxb = taxable_income * 0.15
		taxa = taxable_income - 33950
		tax = taxa * 0.25
		total_tax =   tax + taxb
		print("your tax is",total_tax)

	elif taxable_income > 82251 and taxable_income < 171550:
		taxable_income = taxable_income - 8350
		taxb = taxable_income * 0.15
		taxa = taxable_income - 33950
		tax = taxa * 0.25
		taxa = taxa - 82250
		taxc = taxa * 0.28
		total_tax =   taxc + tax +taxb
		print("your tax is",total_tax)

	elif taxable_income > 171551 and taxable_income < 372950:
		taxable_income = taxable_income - 8350
		taxb = taxable_income * 0.15
		taxa = taxable_income - 33950
		tax = taxa * 0.25
		taxa = taxa - 82250
		taxc = taxa * 0.28
		taxd = taxa - 171550
		taxd = taxd * 0.33
		total_tax =  tax + taxd + taxc + taxb
		print("your tax is",total_tax)

	elif taxable_income > 372951:
		taxable_income = taxable_income - 8350
		taxb = taxable_income * 0.15
		taxa = taxable_income - 33950
		tax = taxa * 0.25
		taxa = taxa - 82250
		taxc = taxa * 0.28
		taxd = taxa - 171550
		taxd = taxd * 0.33
		taxe = taxd - 372950
		taxe = taxe* 0.35
		total_tax =  tax + taxe + taxd + taxc + taxb
		print("your tax is",total_tax)
if user_input == 1:
	if taxable_income > 0 and taxable_income < 16700:
		tax = taxable_income * 0.10
		print("your tax is",tax)
	elif taxable_income > 16701 and taxable_income < 67900:
		tax_for_10_percent = 16700 * 0.10
		taxable_income = taxable_income - 16700
		tax = taxable_income * 0.15
		total_tax =  tax_for_10_percent  + tax
		print("your tax is",total_tax)
	elif taxable_income > 67901 and taxable_income < 137050:
		taxable_income = taxable_income - 16700
		taxb = taxable_income * 0.15
		taxa = taxable_income - 67900
		tax = taxa * 0.25
		total_tax =   tax + taxb
		print("your tax is",total_tax)
	elif taxable_income > 137051 and taxable_income < 208850:
		taxable_income = taxable_income - 16700
		taxb = taxable_income * 0.15
		taxa = taxable_income - 67900
		tax = taxa * 0.25
		taxa = taxa - 137050
		taxc = taxa * 0.28
		total_tax =   taxc + tax +taxb
		print("your tax is",total_tax)
	elif taxable_income > 208851 and taxable_income < 372950:
		taxable_income = taxable_income - 16700
		taxb = taxable_income * 0.15
		taxa = taxable_income - 67900
		tax = taxa * 0.25
		taxa = taxa - 137050
		taxc = taxa * 0.28
		taxd = taxa - 208850
		taxd = taxd * 0.33
		total_tax =  tax + taxd + taxc + taxb
		print("your tax is",total_tax)

