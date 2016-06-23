from pprint import pprint

"""
    Given an MxN matrix if a zero is found, turn the row and column to zero
"""


def zero_matrix(matrix):
    zero_rows = set()
    zero_columns = set()
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 0:
                zero_columns.add(j)
                zero_rows.add(i)

    # zero column
    for column in zero_columns:
        for row in matrix:
            row[column] = 0

    # zero row
    for row in zero_rows:
        matrix[row] = [0] * len(matrix[row])

    return matrix


def main():
    matrix = [[1, 2], [3, 4]]
    output = zero_matrix(matrix)
    output = [str(i) for i in output]
    print('\n'.join(output))
    print()
    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    output = zero_matrix(matrix)
    output = [str(i) for i in output]
    print('\n'.join(output))
    print()
    matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
    output = zero_matrix(matrix)
    output = [str(i) for i in output]
    print('\n'.join(output))
    print()
    matrix = [[1, 2, 3], [4, 5, 6], [0, 8, 9]]
    output = zero_matrix(matrix)
    output = [str(i) for i in output]
    print('\n'.join(output))
    print()
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 0, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    output = zero_matrix(matrix)
    output = [str(i) for i in output]
    print('\n'.join(output))
    print()


if __name__ == '__main__':
    main()
