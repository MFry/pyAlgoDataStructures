"""

"""
import unittest


def sort_scores(unsorted_scores, highest_possible_scores):
    counted_scores = [0] * (highest_possible_scores + 1)
    for score in unsorted_scores:
        counted_scores[score] += 1
    sorted_scores = []
    for i, scores in enumerate(counted_scores):
        for _ in range(scores):
            sorted_scores.append(i)

    return sorted_scores


class MyTestCases(unittest.TestCase):
    def test_sort_scores(self):
        test = [5, 9, 10, 3, 12]
        self.assertEqual(sort_scores(test, 15), sorted(test))
