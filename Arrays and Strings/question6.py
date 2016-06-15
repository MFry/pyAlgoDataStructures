from pprint import pprint

"""
 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the
  image by 90 degrees. Can you do this in place
"""


def rotate_90_degrees(matrix):
    # rotate matrix in rings
    # 4 rotations, one in each corner
    # Rotate top
    length = len(matrix) - 1
    ring = 0
    while ring < len(matrix):
        i = ring
        while i < length - ring:
            t = matrix[ring][i]
            matrix[ring][i] = matrix[length - i][ring]
            matrix[length - i][ring] = matrix[length - ring][length - i]
            matrix[length - ring][length - i] = matrix[i][length - ring]
            matrix[i][length - ring] = t
            i += 1
        ring += 1
    return matrix


test = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
pprint(rotate_90_degrees(test))
