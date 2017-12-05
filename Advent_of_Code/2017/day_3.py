import unittest


def distance_from_spiral_center(number):
    ring = 1
    total_rings = 0
    while ring**2 < number:
        ring += 2
        total_rings += 1
    ring_corner_value = ring ** 2
    while ring_corner_value > number:
        ring_corner_value -= (ring-1)
    distance = total_rings + abs(number - (ring_corner_value+((ring-1)//2)))
    return distance


class MyTestCases(unittest.TestCase):
    def test_distance_from_spiral_center(self):
        test = 1
        self.assertEquals(distance_from_spiral_center(test), 0)
        test = 12
        self.assertEquals(distance_from_spiral_center(test), 3)
        test = 23
        self.assertEquals(distance_from_spiral_center(test), 2)
        test = 1024
        self.assertEquals(distance_from_spiral_center(test), 31)


if __name__ == '__main__':
    puzzle_input = 312051
    print(distance_from_spiral_center(puzzle_input))
