"""
Part 1
Input: [2, 4, 5, 9, 12, 17] , num
output: index
"""


def binary_search(arr, num):
    lower, upper = 0, len(arr) - 1
    while lower <= upper:
        mid = (upper + lower) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1


"""
Part 2
Input:  [9, 12, 17, 2, 4, 5], num
output: index
"""


# [90, 1,2,3]
# [60,70,80,90,1]
# [2,4]
def shifted_binary_search(arr, num):
    # find if the array is shifted
    lower, upper = 0, len(arr) - 1  # L: 0,3,5   U: 5
    while lower < upper:  # T
        mid = (upper + lower) // 2  # M: 2, 4
        if arr[lower] < arr[mid]:  # 60 < 80, 80 < 90
            lower = mid
        else:
            upper = mid - 1
    # upper == lower 0 , 4
    shift = upper

