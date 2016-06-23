"""
http://www.topcoder.com/tc?module=Static&d1=tournaments&d2=tco04&d3=alg_room3_analysis
https://community.topcoder.com/stat?c=problem_statement&pm=2945&rd=5884
"""


def original(blurred):
    # clean the input
    blurred = [[int(i) for i in row] for row in blurred]
    original_image = [[False] * len(blurred[0])] * len(blurred)

    def sweep(center_i, center_j, total_fills):
        white_fill = []
        # start in the top left corner
        i = center_i - 1
        while i <= center_i + 1:
            j = center_j - 1
            while j <= center_j + 1:
                print(len(blurred)-2)
                print(len(blurred[0])-2)
                if i <= 0 or i > len(blurred)-2 or j <= 0 or j < len(blurred[0])-2:
                    pass
                else:
                    # hit
                    white_fill.append((i, j))
                    total_fills -= 1
                    if total_fills == 0:
                        break
                j += 1
            i += 1
        return white_fill

    def update(center_i, center_j):
        i = center_i - 1
        while i <= center_i + 1:
            j = center_j - 1
            while j <= center_j + 1:
                if i < 1 or i > len(blurred)-2 or j < 1 or j < (blurred[0])-2:
                    blurred[i][j] -= 1

    for i, row in enumerate(blurred):
        for j, _ in enumerate(row):
            to_fill = sweep(i, j, int(blurred[i][j]))
            # update
            for coords in to_fill:
                original_image[coords[0]][coords[1]] = 1
                update(*coords)
    return original_image

test = ['1221',
        '1221',
        '1221']

print(original(test))
