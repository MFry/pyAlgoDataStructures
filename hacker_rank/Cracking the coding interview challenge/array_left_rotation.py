import unittest


def array_left_rotation(a, n, k):
    rotated_a = []
    start = k % n
    end = start
    while start < len(a):
        rotated_a.append(a[start])
        start += 1
    start = 0
    while start < end:
        rotated_a.append(a[start])
        start += 1
    return rotated_a


class MyTestCases(unittest.TestCase):

    def test_array_left_rotation(self):
        n, k = 5,4
        test_array = [1, 2, 3, 4, 5]
        self.assertEqual(array_left_rotation(test_array, n, k), [5, 1, 2, 3, 4])

if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k)
    print(*answer, sep=' ')
