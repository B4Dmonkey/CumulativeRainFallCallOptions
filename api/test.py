import unittest
import datetime
from main import payout, rainfall_index


class TestAPI(unittest.TestCase):

    def test_payoutFormula(self):
        strike = 16
        ex = 24
        notional = 25000
        self.assertEqual(payout(strike, ex, notional), 50000)

    def test_rainfall_index(self):
        start = datetime.date(2022, 6, 1)
        end = datetime.date(2022, 6, 2)
        index = rainfall_index(start, end)


if __name__ == '__main__':
    unittest.main()
