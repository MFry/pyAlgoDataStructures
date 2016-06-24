"""
http://www.topcoder.com/tc?module=Static&d1=tournaments&d2=tco04&d3=alg_room3_analysis
https://community.topcoder.com/stat?c=problem_statement&pm=2945&rd=5884
"""


def original(blurred):
    blurred = [[int(i) for i in row] for row in blurred]
    original = [['.'] * len(blurred[0]) for _ in range(len(blurred))]

    def find_white(center_i, center_j, count):
        """

            D D D
            D X C
            D C C

            We are essentially just checking C's and ignoring D's
        """
        i = center_i + 1
        j = center_j + 1
        to_fill = []
        while j <= center_j + 1:
            if i == 0 or i > len(blurred) - 2 or j == 0 or j > len(blurred[i]) - 2:
                pass
            else:
                if original[i][j] != '#':
                    to_fill.append((i, j))
                    count -= 1
                    if count == 0:
                        break
            j += 1
        return to_fill

    def update(center_i, center_j):
        # update the averages for the rest of the blurred image
        i = center_i - 1
        while i <= center_i + 1:
            j = center_j - 1
            while j <= center_j + 1:
                if i < 0 or i >= len(blurred) or j < 0 or j >= len(blurred[i]):
                    continue
                else:
                    if blurred[i][j] > 0:
                        blurred[i][j] -= 1
                j += 1
            i += 1

    for i, row in enumerate(blurred):
        for j, _ in enumerate(row):
            if blurred[i][j] != 0:
                to_fill = find_white(i, j, blurred[i][j])
                for x, y in to_fill:
                    original[x][y] = '#'
                    update(x, y)

    # convert list into a readable output
    out = ''
    for row in original:
        for ele in row:
            out += ele
        out += '\n'

    return out


test = ['1221',
        '1221',
        '1221']

print(original(test))

test = ["0011212121100",
        "0123333333210",
        "0123333333210",
        "1233333333321",
        "1233333333321",
        "1233333333321",
        "0112121212110"]

print(original(test))

test = ["1233321000000000123332100000000000000000000",
        "1244422233222332334343323322232112332223321",
        "1255523344343443545343434434343233432334432",
        "0033303455465775633011445546454355753457753",
        "0033303333364543533011433336333364521346542",
        "0033303455464532445343545546454355753446542",
        "0022202344342200234343434434343233432323221",
        "0011101233221100123332223322232112332211111"]

print(original(test))
