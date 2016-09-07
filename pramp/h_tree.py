from math import sqrt

"""
 |----|     |-----|
   |           |
   |-----------|
   |           |
 |----|     |-----|
"""
def drawLine(x1, x2, y1, y2):
    pass

def h_tree_vertical(x, y, starting_length, depth):
    bottom_y = y - (starting_length / 2)
    top_y = y + (starting_length / 2)
    drawLine(x, x, bottom_y, top_y)
    h_tree_horizontal(x, top_y, starting_length / sqrt(2), depth - 1)
    h_tree_horizontal(x, bottom_y, starting_length / sqrt(2), depth - 1)


def h_tree_horizontal(x, y, starting_length, depth):
    if depth == 0:
        return
    left_x = x - (starting_length / 2)
    right_x = x + (starting_length / 2)
    drawLine(left_x, right_x, y, y)
    h_tree_vertical(left_x, y, starting_length, depth)
    h_tree_vertical(right_x, y, starting_length, depth)


def h_tree(x, y, starting_length, depth):
    if depth == 0:
        return

    left_x = x - (starting_length / 2)
    right_x = x + (starting_length / 2)
    bottom_y = y - (starting_length / 2)
    top_y = y + (starting_length / 2)
    drawLine(left_x, right_x, y, y)
    drawLine(left_x, left_x, bottom_y, top_y)
    drawLine(right_x, right_x, bottom_y, top_y)
    # 4 h tree calls
    #h_tree()

"""
    Space
    O(d)
    Runtime
    O(4 ^ d)

"""

