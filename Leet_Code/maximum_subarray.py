import unittest


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur_sum = 0
    max_sum = float('-inf')
    for num in nums:
        if cur_sum + num > max_sum:
            max_sum = cur_sum + num
        if cur_sum + num < 0:
            cur_sum = 0
        else:
            cur_sum += num
    return max_sum


class MyTestCases(unittest.TestCase):

    def test_maxSubArray(self):
        test_case = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(maxSubArray(test_case), 6)


