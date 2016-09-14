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
        x_i, y_i = find_intersection([(0,0), (a,b)], [(x, y), (x-a, y+b)])
        self.assertEqual((x_i, y_i), (4,4))
        x_i / (x_i-x-a)


        x, y = 100, 200
        a, b = 10, 20
        x_i, y_i = find_intersection([(0, 0), (a,b)], [(x, y), (x-a, y+b)])
        self.assertEqual((x_i, y_i), (10, 20))


5, 3
1, 1
# 4, -1

100, 200
10, 20
# 10, 0
# print('{:.13f}\n{:.13f}\n'.format(n,k))
