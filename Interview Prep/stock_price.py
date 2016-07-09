import unittest

"""
    Problem 1
    Greedy
"""

def brute_get_max_profits(yesterday_prices):
    """
        Brute Force method
    :param yesterday_prices:
    :return:
    """
    max_price = float('-inf')
    for i, buy_price in enumerate(yesterday_prices):
        best_price = float('-inf')
        for sell_price in yesterday_prices[i + 1:]:
            if best_price < sell_price - buy_price:
                best_price = sell_price - buy_price
        if best_price > max_price:
            max_price = best_price
    return max_price


def get_max_profits(yesterday_prices):
    """
        Greedy Algorithm O(n)
    :param yesterday_prices:
    :return:
    """
    if len(yesterday_prices) < 2:
        raise IndexError('Calculating profit requires at least two values')
    min_buy = float('inf')
    max_price = float('-inf')
    for sell_price in yesterday_prices:
        if sell_price - min_buy > max_price:
            max_price = sell_price - min_buy
        if min_buy > sell_price:
            min_buy = sell_price
    return max_price


class MyTestCase(unittest.TestCase):
    def test_get_max_profits(self):
        check_price_yesterday = [10, 7, 5, 8, 11, 9]
        self.assertEqual(brute_get_max_profits(check_price_yesterday), 6)
        self.assertEqual(get_max_profits(check_price_yesterday), 6)
        check_price_yesterday = [10, 11, 12, 50, 60, 100]
        ans = brute_get_max_profits(check_price_yesterday)
        self.assertEqual(get_max_profits(check_price_yesterday), ans)
