import unittest


def candies(seq):
    to_dist = [1] * len(seq)
    for i in range(1, len(seq)):
        if seq[i] > seq[i - 1]:
            to_dist[i] = to_dist[i - 1] + 1
    for i in range(len(seq) - 2, -1, -1):
        if seq[i] > seq[i + 1]:
            if to_dist[i] <= to_dist[i + 1]:
                to_dist[i] = to_dist[i + 1] + 1
    return to_dist


class MyTestCases(unittest.TestCase):
    def test_candies(self):
        test1 = [1, 2, 2]
        self.assertEqual(candies(test1), [1, 2, 1])
        self.assertEqual(sum(candies(test1)), 4)
        test2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        self.assertEqual(candies(test2), [1, 2, 1, 2, 1, 2, 3, 4, 2, 1])
        self.assertEqual(sum(candies(test2)), sum([1, 2, 1, 2, 1, 2, 3, 4, 2, 1]))
        test3 = [5, 4, 3, 2, 1]
        self.assertEqual(candies(test3), [5, 4, 3, 2, 1])
        self.assertEqual(sum(candies(test3)), sum([5, 4, 3, 2, 1]))


if __name__ == '__main__':
    _ = int(input())
    ratings = []
    for i in range(_):
        ratings.append(int(input()))
    candies_distribution = candies(ratings)
    print(sum(candies_distribution))
