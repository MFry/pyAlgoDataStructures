import unittest


def get_max_profits(yesterday_prices):
    max_price = float('-inf')
    for i, buy_price in enumerate(yesterday_prices):
        best_price = float('-inf')
        for sell_price in yesterday_prices[i + 1:]:
            if best_price < sell_price - buy_price:
                best_price = sell_price - buy_price
        if best_price > max_price:
            max_price = best_price
    return max_price


class MyTestCase(unittest.TestCase):
    def test_get_max_profits(self):
        check_price_yesterday = [10, 7, 5, 8, 11, 9]
        self.assertEqual(get_max_profits(check_price_yesterday), 6)
