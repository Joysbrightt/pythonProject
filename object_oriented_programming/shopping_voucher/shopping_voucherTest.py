import unittest
from . import Shopping

class shopping_voucher(unittest.TestCase):
    def setUp(self) -> None:
        print("I run before")

    def tearDown(self) -> None:
        print("I run after")


    def test_something(self):
        print('running a programme')



if __name__ == '__main__':
    unittest.main()
