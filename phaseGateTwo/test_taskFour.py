import unittest
import taskFour

class TestTaskFour(unittest.TestCase):
	def test_that_sumString_function_exist(self):
		taskFour.sumString("2","2")
	def test_that_sumString_function_returns(self):
		self.assertEqual(taskFour.sumString("2","2"),"4.0")
	def test_that_sumString_function_returns_if_negative(self):
		self.assertEqual(taskFour.sumString("-2","-2"),"-4.0")
	def test_that_sumString_function_raise_error_if_integer_inputed(self):
		self.assertRaises(TypeError,taskFour.sumString,2,2)
	def test_that_sumString_function_returns_if_decimal_inputed(self):
		self.assertEqual(taskFour.sumString("0.12","0.56"),"0.68")