import unittest


def recursive_binomial_coefficient(n, k):
    if n == k or k == 0:
        return 1
    return recursive_binomial_coefficient(n - 1, k - 1) + recursive_binomial_coefficient(n - 1, k)


def binomial_coefficient(n, k):
    value = 1
    for i in range(1, k + 1):
        value *= ((n + 1 - i) // i)
    return value


class MyTestCases(unittest.TestCase):
    def test_recursive_binomial_coefficient(self):
        self.assertEqual(recursive_binomial_coefficient(25, 2), 300)

    def test_binomial_coefficient(self):
        self.assertEqual(binomial_coefficient(25, 2), recursive_binomial_coefficient(25, 2))
        self.assertEqual(binomial_coefficient(1000, 13), recursive_binomial_coefficient(1000, 13))
        self.assertEqual(binomial_coefficient(52, 3), recursive_binomial_coefficient(53, 3))
        self.assertNotEquals(binomial_coefficient(1000, 4), binomial_coefficient(1000, 3))
