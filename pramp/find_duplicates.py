def find_dups(arr1, arr2):  # [1,2,3,4] [3,4,5,6,7]
    """
     input: Arr1 and Arr2 of lengths n and m
     output: solution of values within both arrays
    1, m == n
    Time: O(m)
    :param arr1:
    :param arr2:
    :return:
    """
    if len(arr1) == 0 or len(arr2) == 0:
        return []
    i_1, i_2 = 0, 0  # i_1, i_2 = 0,0| 1,0, 2,0 | 3,1 | 4,1
    solution = []  # solution = [] | [3] | [3,4]
    while True:
        if i_1 >= len(arr1) or i_2 >= len(arr2):  # F,F,F,F, T
            break
        if arr1[i_1] == arr2[i_2]:  # 1 != 3 | 2 != 3 | 3 == 3 | 4 == 4
            solution.append(arr1[i_1])
            i_1 += 1
            i_2 += 1
        elif arr1[i_1] < arr2[i_2]:  # T | T
            i_1 += 1
        else:
            i_2 += 1

    return solution


def binary_search(arr, val):
    """
    returns: index or the crossover point
    """
    lower, upper = 0, len(arr) - 1
    while lower < upper:
        mid = (upper + lower) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            lower = mid + 1
        else:
            upper = mid - 1
    return lower


def find_dups_2(large_arr, small_arr):
    """

    2, m >> n
    time O(lg(m)+n)
    :param large_arr:
    :param small_arr:
    :return:
    """
    s_i, l_i = 0, binary_search(large_arr, small_arr[0])
    solution = []
    while True:
        if l_i >= len(large_arr) or s_i >= len(small_arr):
            break
        if large_arr[l_i] == small_arr[s_i]:
            solution.append(small_arr[s_i])
            l_i += 1
            s_i += 1
        elif large_arr[l_i] < small_arr[s_i]:
            l_i += 1
        else:
            s_i += 1

    return solution