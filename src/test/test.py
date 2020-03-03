import unittest
from src import main


class TestHelloWorld(unittest.TestCase):

    def test_forex_data_returns_200(self):
        self.assertEqual(main.get_forex_data("GBP").status_code, 200)

    def test_forex_data_returned_matches_currency_param(self):
        self.assertAlmostEqual(main.get_forex_data("USD"), {"symbols_returned": 150, "base": "USD"})
        self.assertAlmostEqual(main.get_forex_data("GBP"), {"symbols_returned": 150, "base": "GBP"})

if __name__ == '__main__':
    unittest.main()
