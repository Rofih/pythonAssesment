import unittest
import investment

class TestInveztment(unittest.TestCase):
	def test_that_future_investment_function_exist(self):
		investment.future_investment(1500,5,6)
	def test_that_future_investment_function_can_take_in_non_integers(self):
		investment.future_investment(1400.7,4.2,6.5)
	def test_that_future_investment_function_raise_error_with_negative_input(self):
		self.assertRaises(ValueError,investment.future_investment(-1557,-5,-56))