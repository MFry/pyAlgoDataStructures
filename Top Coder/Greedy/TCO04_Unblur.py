"""
http://www.topcoder.com/tc?module=Static&d1=tournaments&d2=tco04&d3=alg_room3_analysis
https://community.topcoder.com/stat?c=problem_statement&pm=2945&rd=5884
"""


def original(blurred):
    original_image = [[False] * len(blurred[0])] * len(blurred)

    def sweep(center_i, center_j):
        # start in the top left corner
        i = center_i - 1
        j = center_j - 1
        for i in range(center_i + 1):
            for j in range(center_j + 1):
                if i < 0 or i > len(blurred) or j < 0 or j < (blurred[0]):
                    continue

    blurred = [[i for i in row] for row in blurred]
    for i, row in enumerate(blurred):
        for j, _ in enumerate(row):
            sweep(i, j)


test = ['1221',
        '1221',
        '1221']

print(original(test))
