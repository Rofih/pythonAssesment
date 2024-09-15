import unittest
import discount

class TestDiscount(unittest.TestCase):
	def test_that_my_discount_function_exist(self):
		discount.my_discount(500,20)
	def test_that_my_discount_function_returns_discounted_value(self):
		self.assertEqual(discount.my_discount(150,15),127.5)
	def test_that_my_discount_function_raise_error_with_negative_values(self):
		self.assertRaises(ValueError,discount.my_discount(-2344,-32))