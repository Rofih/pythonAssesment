import unittest
import swap

class TestSwap(unittest.TestCase):
	def test_swapper_function_exist(self):
		swap.swapper(number = [1,2,3,4,5,6])
	def test_swapper_function_returns(self):
		self.assertEqual(swap.swapper([1,2,3,4,5,6]),[2,1,4,3,5,6])