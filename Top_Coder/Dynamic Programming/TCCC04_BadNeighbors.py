import unittest

"""
    Problem Statement: https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009
"""


def maxDonations(donations):
    computed_donations = [(0, 0)] * len(donations)
    computed_donations[0] = [(donations[0], 0)]
    max = 0
    for i, donate in enumerate(donations[1:]):
        conflict = i - 1
        # TODO: Handle the end edge case
        j = conflict - 1
        donated = donate
        prev_donor = i
        while j >= 0:
            if computed_donations[j][1] != conflict:
                if donated < computed_donations[j][0] + donate:
                    donated = computed_donations[j][0] + donate
                    prev_donor = j
            j -= 1
        if donated > max:
            max = donated
        computed_donations[i] = (donated, prev_donor)
    return max


class MyTestCase(unittest.TestCase):
    def test_maxDonations(self):
        self.assertTrue(19, maxDonations([10, 3, 2, 5, 7, 8]))
        self.assertTrue(15, maxDonations([11, 15]))
        self.assertTrue(21, maxDonations([7, 7, 7, 7, 7, 7, 7]))
        self.assertTrue(16, maxDonations([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
        self.assertTrue(4, maxDonations([1, 1, 0, 1, 1, 0, 1, 2, 0]))
        self.assertTrue(2926, maxDonations([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
                                            6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
                                            52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]))


if __name__ == '__main__':
    unittest.main()
