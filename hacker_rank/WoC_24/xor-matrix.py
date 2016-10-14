from pprint import pprint
from operator import xor

test = [6, 7, 1, 3]


def get_xor_matrix(row, total_columns):
    matrix = [row]
    for i in range(total_columns):
        temp = []
        for j in range(len(row)):
            left = j
            right = j + 1
            if right == len(row):
                right = 0
            test = matrix[-1]
            temp.append(xor(matrix[-1][left], matrix[-1][right]))
        matrix.append(temp)
    return matrix


pprint(get_xor_matrix(test, 5))
pprint(get_xor_matrix([1, 2, 3, 4, 5], 1000))
