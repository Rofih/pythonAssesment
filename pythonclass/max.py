def get_maximum(first_number, second_number, third_number):
	if first_number > second_number and first_number > third_number:
		return first_number
	if second_number>first_number and second_number>third_number:
		return second_number
	if third_number>first_number and third_number>second_number:
		return third_number

print(get_maximum(52,7,3))



def get_minimum(first_number, second_number, third_number):
	if first_number < second_number and first_number < third_number:
		return first_number
	if second_number < first_number and second_number < third_number:
		return second_number
	if third_number < first_number and third_number < second_number:
		return third_number

print(get_minimum(52,7,3))
	