def my_discount(price,discount):
	if price<0 and discount<0:
		raise ValueError("invalid inputs")
	amount=(discount/100)*price
	return price-amount