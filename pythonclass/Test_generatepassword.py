import string
import unittest
import generatepassword

class TestGeneratePassword(unittest.TestCase):
	
	def test_that_get_password_function_exist(self):
		generatepassword.get_password()
	def test_that_the_length_in_get_password_is_16(self):
		self.assertEqual(len(generatepassword.get_password()),16)
	def test_that_upper_case_is_present_in_get_function(self):
		password = generatepassword.get_password()
		self.assertTrue(any(count for count in password if count.upper()))
	def test_that_lower_case_is_present_in_get_function(self):
		password = generatepassword.get_password()
		self.assertTrue(any(count for count in password if count.lower()))
	def test_that_digit_is_present_in_get_function(self):
		password = generatepassword.get_password()
		self.assertTrue(any(count for count in password if count in string.digits))	