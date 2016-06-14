"""
 https://community.topcoder.com/stat?c=problem_statement&pm=2977&rd=5880
 https://community.topcoder.com/tc?module=Static&d1=match_editorials&d2=tco04_online_rd_3
 http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/

-	Each of the five arguments will contain between 0 and 50 elements inclusive.
-	Each element of each of the arguments will be between 0 and 180,000 inclusive.
-	The elements within each of the arguments will be in strictly increasing order.
"""


def max_credit(judge1, judge2, judge3, judge4, judge5):
    judges = [judge1, judge2, judge3, judge4, judge5]
    #max_size = max(len(judge1), len(judge2), len(judge3), len(judge4), len(judge5))
    #print('Max size:', max_size)
    intervals = [(-1, -1)]


    def find_smallest_interval(judges):
        interval_found = (min([j[0] for j in judges]), min([j[0] for j in judges]))
        votes = [False * 5]
        while True:
            for i, judge in enumerate(judges):
                if judge:
                    for vote in judge:
                        if vote > interval_found[1]:
                            break
                        else:
                            votes[i] = True
            i = 0
            for vote in votes:
                i += 1
            if i >= 3:
                break
            else:
                interval_found()
        return interval_found

        # find smallest interval that at least three judges agree upon

        # find next smallest interval until end

