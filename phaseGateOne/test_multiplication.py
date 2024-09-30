import unittest
import multiplication

class TestMultiplication(unittest.TestCase):
	def test_that_multiply_function_exist(self):
		multiplication.multiply(2,3)
	def test_that_multiply_function_returns(self):
		self.assertEqual(multiplication.multiply(2,6),12)
	def test_that_multiply_function_returns(self):
		self.assertEqual(multiplication.multiply(2,4),8)
	def test_that_multiply_function_returns(self):
		self.assertEqual(multiplication.multiply(5,5),25)
	def test_that_multiply_function_returns(self):
		self.assertEqual(multiplication.multiply(12,12),144)
	def test_that_multiply_function_returns_when_negative_numbers_inputed(self):
		self.assertEqual(multiplication.multiply(-5,-5),25)
	def test_that_multiply_function_returns_when_negative_numbers_inputed(self):
		self.assertEqual(multiplication.multiply(-6,2),-12)
	def test_that_multiply_function_returns_when_negative_numbers_inputed(self):
		self.assertEqual(multiplication.multiply(-6,-5),30)