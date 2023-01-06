import unittest
from main import main, payout


class TestAPI(unittest.TestCase):

    def test_payoutFormula(self):
        self.assertTrue(main())

    def test_payoutFormula(self):
        strike = 16
        ex = 0
        notional = 25000
        self.assertEqual(payout(strike, ex, notional), 50000)


if __name__ == '__main__':
    unittest.main()
