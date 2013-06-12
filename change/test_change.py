import unittest
from change import NotFoundsError, give_change

class TestChange(unittest.TestCase):

    def test_value_minor_price(self):
        with self.assertRaises(NotFoundsError):
            give_change(cash=30, total=100)

    def test_value_cash_50_total_20(self):
        change = give_change(cash=50, total=20)
        expected = {
            '10': 3
        }
        self.assertEqual(change, expected)

    def test_value_cash_50_total_15(self):
        change = give_change(cash=50, total=15)
        expected = {
            '10': 3,
            '5': 1
        }
        self.assertEqual(change, expected)

    def test_value_cash_50_total_17_53(self):
        change = give_change(cash=50, total=17.53)
        expected = {
            '10': 3,
            '1': 2,
            '0.1': 4,
            '0.05': 1,
            '0.01': 2

        }
        self.assertEqual(change, expected)

if __name__ == '__main__':
    unittest.main()
