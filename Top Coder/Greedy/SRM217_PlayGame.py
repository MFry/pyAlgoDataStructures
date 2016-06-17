def saveCreatures(your_army, comp_army):
    comp_army.sort(reverse=True)
    your_army.sort()
    used = []
    for piece in comp_army:
        i = -1
        if your_army[i] > piece:
            while i + len(your_army) > 0:
                if your_army[i] <= piece:
                    break
                i -= 1
            used.append(your_army[i + 1])
            your_army.remove(used[-1])
        else:
            your_army = your_army[1:]
    return sum(your_army + used)


you_test = [5, 15, 100, 1, 5]
computer_test = [5, 15, 100, 1, 5]
solution = 120
print(saveCreatures(you_test, computer_test) == solution)

you_test = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
computer_test = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
solution = 0
print(saveCreatures(you_test, computer_test) == solution)
you_test = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
computer_test = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
solution = 99
print(saveCreatures(you_test, computer_test) == solution)
you_test = [651, 321, 106, 503, 227, 290, 915, 549, 660, 115,
            491, 378, 495, 789, 507, 381, 685, 530, 603, 394,
            7, 704, 101, 620, 859, 490, 744, 495, 379, 781,
            550, 356, 950, 628, 177, 373, 132, 740, 946, 609,
            29, 329, 57, 636, 132, 843, 860, 594, 718, 849]
computer_test = [16, 127, 704, 614, 218, 67, 169, 621, 340, 319,
                 366, 658, 798, 803, 524, 608, 794, 896, 145, 627,
                 401, 253, 137, 851, 67, 426, 571, 302, 546, 225,
                 311, 111, 804, 135, 284, 784, 890, 786, 740, 612,
                 360, 852, 228, 859, 229, 249, 540, 979, 55, 82]
solution = 25084
print(saveCreatures(you_test, computer_test) == solution)
