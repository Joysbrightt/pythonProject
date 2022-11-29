import unittest
from . import Accountt


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
      account1 = Accountt.Accountt("AccountName")

      self.assertIsNotNone(account1)
      self.assertIsInstance(account1, Accountt.Accountt)


    def test_that_account_has_a_name(self):

        account1 = Accountt.Accountt("accountName")
        name = account1.name
        self.assertEqual("accountName", name)


    def test_that_account_can_deposit(self):
        accout1 = Accountt.Accountt("accountName")
        accout1.deposit(2000)
        self.assertEqual(2000, accout1.balance)


        def test_that_negative_deposit_raises_error(self):
            accout1 = Accountt.Accountt("accountName")
            accout1.deposit(500)
            accout1.deposit(-1000)
            self.assertRaises(ValueError, accout1.deposit, -1000)

            self.assertEqual(500, accout1.balance)


    def test_that_account_can_be_used_to_recharge(self):
        accout1 = Accountt.Accountt("AccountName")
        accout1.deposit(2000)
        self.assertEqual(2000, accout1.balance)
        accout1.buy_recharge_card(500)
        self.assertEqual(1500, accout1.balance)


    def test_that_account_can_withdraw(self):
        accout1 = Accountt.Accountt("accountName")
        accout1.deposit(2000)
        self.assertEqual(2000, accout1.balance)
        accout1.withdraw(1000)
        self.assertEqual(1000, accout1.balance)
        accout1.deposit(-1000)
        self.assertRaises(ValueError, accout1.deposit, -1000)


    def test_that_account_can_transfer(self):
        accout1 = Accountt.Accountt("accountName")
        account2 = Accountt.Accountt("second_account")
        accout1.deposit(5000)
        self.assertEqual(5000, accout1.balance)
        accout1.make_transfer(2000, account2 )
        self.assertEqual(3000, accout1.balance)
        self.assertEqual(2000, account2.balance)



if __name__ == '__main__':
        unittest.main()
