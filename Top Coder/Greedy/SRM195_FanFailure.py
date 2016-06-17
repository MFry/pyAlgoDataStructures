"""
    https://community.topcoder.com/stat?c=problem_statement&pm=2235&rd=5070
"""


def getRange(capacities, minCooling):
    """

    :param capacities:
    :param minCooling:
    :return:  Maximum Failure Set (MFS) and the Maximum Failure Count (MFC). A MFS is a Failure Set of fans with the
    largest count possible. A set of fans may have more than one MFS. A Failure Set is an MFS if and only
     if there are no Failure Sets with a higher count.
     The MFC is the largest value such that all fan sets with count <= MFC are Failure Sets. In other words,
      any set of fans of size MFC or less can fail, and the system will still be properly cooled by the remaining fans.
    """
    mfs_check = sorted(capacities)
    mfc_check = sorted(capacities, reverse=True)
    total_cooling = sum(capacities)
    mfs = 0
    for capacity in mfs_check:
        if total_cooling - capacity > minCooling:
            mfs += 1
            total_cooling -= capacity
    mfc = 0
    total_cooling = sum(capacities)
    for capacity in mfc_check:
        if total_cooling - capacity > minCooling:
            mfc += 1
            total_cooling -= capacity
        else:
            # We cannot remove any more fans
            break
    return mfs, mfc


test_cap = [1, 2, 3]
test_cool = 2
solution = (2, 1)
print(getRange(test_cap, test_cool) == solution)
test_cap = [8,5,6,7]
test_cool = 22
solution = (0, 0)
print(getRange(test_cap, test_cool) == solution)
test_cap = [676, 11, 223, 413, 823, 122, 547, 187, 28]
test_cool = 1000
solution = (7, 2)
print(getRange(test_cap, test_cool) == solution)