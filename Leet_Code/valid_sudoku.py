for i in range(9):
    print('block ', i)
    for j in range(9):
        squareRow = (j // 3) + 3*(i // 3)
        squareCol = (j % 3) + 3*(i % 3)
        print(squareRow, squareCol)
