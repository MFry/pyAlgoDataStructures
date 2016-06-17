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
    return mfs, mfc


test_cap = [1, 2, 3]
test_cool = 2
solution = [2, 1]
print(getRange(test_cap, test_cool) == solution)
