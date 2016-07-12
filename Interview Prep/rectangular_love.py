import unittest
"""
Problem 6:
"""

sample_rectangle = {
    # bottom left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4
}


def love_match(rectangle_1, rectangle_2):
    """
        Find the intersection between two rectangles
    :param rectangle_1: dict
    :param rectangle_2: dict
    :return:
    """

    def get_coords(rectangle):
        """
            Given a dictionary with keys
                left_x, bottom_y, width and height this will return the
                x1,x2,y1,y2 coordinates
        :param rectangle:
        :return:
        """
        x1 = rectangle['left_x']
        x2 = x1 + rectangle['width']
        y1 = rectangle['bottom_y']
        y2 = y1 + rectangle['height']
        return x1, y1, x2, y2

    def find_line_overlap(r1_p1, r1_p2, r2_p1, r2_p2):
        if r1_p1 <= r2_p1 <= r1_p2:
            overlap_p1 = r2_p1
        elif r2_p1 <= r1_p1 <= r2_p2:
            overlap_p1 = r1_p1
        else:
            # There is no intersection
            return None

        if r2_p2 >= r1_p2:
            overlap_p2 = r1_p2
        else:
            overlap_p2 = r2_p2
        return overlap_p1, overlap_p2

    r1_x1, r1_y1, r1_x2, r1_y2 = get_coords(rectangle_1)
    r2_x1, r2_y1, r2_x2, r2_y2 = get_coords(rectangle_2)

    solution_rectangle_x = find_line_overlap(r1_x1, r1_x2, r2_x1, r2_x2)
    solution_rectangle_y = find_line_overlap(r1_y1, r1_y2, r2_y1, r2_y2)

    if solution_rectangle_x is None or solution_rectangle_y is None:
        return None
    intersection_rectangle = {'left_x': solution_rectangle_x[0],
                              'bottom_y': solution_rectangle_y[0],
                              'width': solution_rectangle_x[1] - solution_rectangle_x[0],
                              'height': solution_rectangle_y[1] - solution_rectangle_y[0]}
    return intersection_rectangle


class MyTestCase(unittest.TestCase):
    def test_find_x_overlap(self):
        def find_line_overlap(r1_p1, r1_p2, r2_p1, r2_p2):
            if r1_p1 <= r2_p1 <= r1_p2:
                overlap_p1 = r2_p1
            elif r2_p1 <= r1_p1 <= r2_p2:
                overlap_p1 = r1_p1
            else:
                # There is no intersection
                return None

            if r2_p2 >= r1_p2:
                overlap_p2 = r1_p2
            else:
                overlap_p2 = r2_p2
            return overlap_p1, overlap_p2

        # x-axis line test/y-axis line test
        self.assertEqual(find_line_overlap(5, 10, 7, 12), (7, 10))
        self.assertEqual(find_line_overlap(7, 12, 5, 10), (7, 10))
        self.assertEqual(find_line_overlap(2, 5, 7, 8), None)
        self.assertEqual(find_line_overlap(7, 8, 2, 5), None)

    def test_love_match(self):
        test_rectangle_1 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 5,
            'height': 5
        }
        test_rectangle_2 = {
            'left_x': 7,
            'bottom_y': 5,
            'width': 8,
            'height': 15
        }
        correct_rectangle = {
            'left_x': 7,
            'bottom_y': 5,
            'width': 3,
            'height': 2
        }
        answer_rectangle = love_match(test_rectangle_1, test_rectangle_2)
        for key in correct_rectangle:
            self.assertEqual(correct_rectangle[key],
                             answer_rectangle[key])
        test_rectangle_1 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 5,
            'height': 8
        }
        test_rectangle_2 = {
            'left_x': 6,
            'bottom_y': 3,
            'width': 1,
            'height': 5
        }
        correct_rectangle = {
            'left_x': 6,
            'bottom_y': 3,
            'width': 1,
            'height': 5
        }
        answer_rectangle = love_match(test_rectangle_1, test_rectangle_2)
        for key in correct_rectangle:
            self.assertEqual(correct_rectangle[key],
                             answer_rectangle[key])
