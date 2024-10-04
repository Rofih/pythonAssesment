import unittest
import square

class TestSquare(unittest.TestCase):
	def test_divide_or_square_function_exist(self):
		square.divide_or_square(10)
	def test_that_divide_or_square_function_returns_squareroot_result(self):
		self.assertEqual(square.divide_or_square(25),5)
	def test_that_divide_or_square_function_raise_error_with_squareroot_of_negative_values(self):
		self.assertRaises(ValueError,square.divide_or_square,-25)
	def test_that_divide_or_square_function_returns_squareroot_of_non_integer_inputs(self):
		self.assertEqual(square.divide_or_square(0.2),0.04)
	def test_that_divide_or_square_function_returns_if_value_divisible_by_5(self):
		self.assertEqual(square.divide_or_square(10),3.1622776601683795)
	def test_that_divide_or_square_function_returns_number_divided_by_5_if_number_is_not_divisible_by_5_without_remainder(self):
		self.assertEqual(square.divide_or_square(7),1.4)
	def test_that_divide_or_square_function_raise_error_with_string(self):
		self.assertRaises(TypeError,square.divide_or_square,'number')