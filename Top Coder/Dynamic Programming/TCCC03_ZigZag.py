import unittest


def ZigZag(sequence):
    computed_lengths = [(-1, 0)] * len(sequence)
    global_max_length = -1
    for i, element in enumerate(sequence):
        j = i - 1
        max_length = 1
        signed_diff = 0
        while j >= 0:
            diff = sequence[i] - sequence[j]
            if diff > 0 >= computed_lengths[j][1]:
                if computed_lengths[j][0] + 1 > max_length:
                    max_length = computed_lengths[j][0] + 1
                    signed_diff = 1
            elif diff < 0 <= computed_lengths[j][1]:
                if computed_lengths[j][0] + 1 > max_length:
                    max_length = computed_lengths[j][0] + 1
                    signed_diff = -1
            j -= 1
        if global_max_length < max_length:
            global_max_length = max_length
        computed_lengths[i] = (max_length, signed_diff)

    return max_length


print(ZigZag([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
print(ZigZag([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(ZigZag([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]))
print(ZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
              600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
              67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
              477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
              249, 22, 176, 279, 23, 22, 617, 462, 459, 244]))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
