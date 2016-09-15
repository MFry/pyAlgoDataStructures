from math import sqrt, ceil
import sys, unittest


def is_repeating(s, sub):
    if len(sub) == 0 or len(s) == 0:
        raise Exception('Invalid input pair: {}, {}'.format(s, sub))
    for i in range(len(s)):
        if s[i] != sub[i % len(sub)]:
            return False
    return True


def largest_commutative_permutations(s, m):
    factors = [i for i in range(1, ceil(sqrt(len(s))) + 1) if len(s) % i == 0] + [len(s)]
    for factor in factors:
        substring = s[:factor]
        if is_repeating(s, substring):
            return m // factor


class MyTestCases(unittest.TestCase):
    def test_largest_commutative_permutations(self):
        s = 'aaaa'
        m = 6
        self.assertEqual(largest_commutative_permutations(s, m), 6)
        s = 'baab'
        m = 5
        self.assertEqual(largest_commutative_permutations(s, m), 1)
        s = 'abcdefghijklmnopqrstuvwxyz'
        m = 27
        self.assertEqual(largest_commutative_permutations(s, m), 1)
        s = 'abab'
        m = 3
        self.assertEqual(largest_commutative_permutations(s, m), 1)


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    print(largest_commutative_permutations(s, m) % 1000000007)
