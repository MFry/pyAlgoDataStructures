"""
 Orthogonal vectors: http://mathworld.wolfram.com/PerpendicularVector.html
 Line-Line Intersection: https://www.topcoder.com/community/data-science/data-science-tutorials/geometry-concepts-line-intersection-and-its-applications/
"""
import unittest


def find_intersection(line1, line2):
    (x1, y1), (x2, y2) = line1
    A_1 = y2 - y1
    B_1 = x1 - x2
    C_1 = A_1*x1 +B_1*y1

    (x1, y1), (x2, y2) = line2
    A_2 = y2 - y1
    B_2 = x1 - x2
    C_2 = A_2*x1 + B_2*y1
    det = A_1*B_2 - A_2*B_1
    x_i = (B_2*C_1 - B_1*C_2)/det
    y_i = (A_1*C_2 - A_2*C_1)/det
    return x_i, y_i


class MyTestCases(unittest.TestCase):

    def test_find_intersection(self):
        x, y = 5, 3
        a, b = 1, 1
        x_i, y_i = find_intersection([(0, 0), (a, b)], [(x, y), (x - b, y + a)])
        self.assertEqual((x_i, y_i), (4, 4))
        self.assertEqual((x_i / a, (x - x_i) / -b), (4.0, -1.0))

        x, y = 100, 200
        a, b = 10, 20
        x_i, y_i = find_intersection([(0, 0), (a, b)], [(x, y), (x - b, y + a)])
        self.assertEqual((x_i, y_i), (100, 200))
        self.assertEqual((x_i / a, (x - x_i) / -b), (10.0, 0.0))

        x, y = 10, 20
        a, b = 5, 4
        x_i, y_i = find_intersection([(0, 0), (a, b)], [(x, y), (x - b, y + a)])
        print((x_i, y_i))
        self.assertEqual((x_i / a, (x - x_i) / -b), (3.1707317073170733, 1.4634146341463414))

        x, y = 5, 5
        a, b = 1, 1
        x_i, y_i = find_intersection([(0, 0), (a, b)], [(x, y), (x - b, y + a)])
        self.assertEqual((x_i / a, (x - x_i) / -b), (5.000000000000, 0.000000000000))


if __name__ == '__main__':
    x, y = [int(i) for i in input().split()]
    a, b = [int(i) for i in input().split()]

    x_i, y_i = find_intersection([(0, 0), (a, b)], [(x, y), (x - b, y + a)])
    n = x_i / a
    k = (x - x_i) / -b
    print('{:.13f}\n{:.13f}\n'.format(n, k))
