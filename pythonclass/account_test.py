import unittest

from pythonclass.account import Account


class MyTestCase(unittest.TestCase):
    def test_that_account_deposit(self):
        amount = 1000
        account = Account("Rofih","09127461933","1234")
        account.deposit(amount)
        result = account.getBalance()
        expected = f'Mr Rofih your balance is {1000}'
        self.assertEqual(expected,result)
    def test_that_i_can_not_deposit_negative_amount(self):
        amount = -1000
        account = Account("Rofih","09127461933","1234")
        account.deposit(500)
        account.deposit(amount)
        result = account.getBalance()
        expected =f'Mr Rofih your balance is {500}'
        self.assertEqual(expected,result)

    def test_that_i_can_withdraw(self):
        amount = 10000
        amount2 = 1000
        account = Account("Rofih", "09127461933","1234")
        account.deposit(amount)
        balance = account.getBalance()
        amount2 = account.withdraw(amount2,"1234")
        balance2 = account.getBalance()
        expected = f'Mr Rofih your balance is {9000}'
        self.assertEqual(expected, balance2)

    def test_that_i_can_not_withdraw_negative_amount(self):
        amount = 10000
        amount2 = -1000
        account = Account("Rofih", "09127461933","1234")
        account.deposit(amount)
        balance = account.getBalance()
        amount2 = account.withdraw(amount2,"1234")
        balance2 = account.getBalance()
        expected = f'Mr Rofih your balance is {10000}'
        self.assertEqual(expected, balance2)

        # add assertion here



