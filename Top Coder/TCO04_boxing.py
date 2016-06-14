"""
 https://community.topcoder.com/tc?module=ProblemDetail&rd=5880&pm=2977
 https://community.topcoder.com/stat?c=problem_statement&pm=2977&rd=5880

-	Each of the five arguments will contain between 0 and 50 elements inclusive.
-	Each element of each of the arguments will be between 0 and 180,000 inclusive.
-	The elements within each of the arguments will be in strictly increasing order.


Hint: Activity Selection, Greedy Algorithm
"""


def max_credit(judge1, judge2, judge3, judge4, judge5):
    judges = [judge1, judge2, judge3, judge4, judge5]
    # max_size = max(len(judge1), len(judge2), len(judge3), len(judge4), len(judge5))
    # print('Max size:', max_size)
    intervals = [(-1, -1)]

    def find_smallest_interval(judges):
        # find smallest interval that at least three judges agree upon
        flattened_votes = set()
        for judge in judges:
            if judge:
                for vote in judge:
                    flattened_votes.add(vote)
        if not flattened_votes:
            return -1, -1
        lower_bound = min(flattened_votes)
        upper_bound = lower_bound
        while True:
            votes = 0
            for judge in judges:
                if judge:
                    for vote in judge:
                        if vote <= upper_bound:
                            votes += 1
                            break
            if votes >= 3:
                return lower_bound, upper_bound
            else:
                flattened_votes -= {upper_bound}
                if flattened_votes:
                    upper_bound = min(flattened_votes)
                else:
                    return -1, -1

    while True:
        interval = find_smallest_interval(judges)
        # find next smallest interval until end
        if interval[0] < 0:
            return intervals[1:]
        intervals.append(interval)
        previous_interval = intervals[-1][1]
        # trim votes
        updated_judgements = []
        for judge in judges:
            if judge:
                i = 0
                for vote in judge:
                    if vote <= previous_interval:
                        i += 1
                    else:
                        break
                updated_judgements.append(judge[i:])
            else:
                updated_judgements.append([])
        judges = updated_judgements

    return intervals[1:]


def main():
    j1 = [1, 2, 3, 4, 5, 6]
    j2 = [1, 2, 3, 4, 5, 6, 7]
    j3 = [1, 2, 3, 4, 5, 6, 7]
    j4 = [0, 1, 2]
    j5 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(max_credit(j1, j2, j3, j4, j5))
    j1 = [1, 2, 3, 4, 5, 6]
    j2 = [1, 2, 3, 4, 5, 6]
    j3 = [1, 2, 3, 4, 5, 6, 7]
    j4 = [0, 1, 2]
    j5 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(max_credit(j1, j2, j3, j4, j5))
    j1 = [100, 200, 300, 1200, 6000]
    j2 = []
    j3 = [900, 902, 1200, 4000, 5000, 6001]
    j4 = [0, 2000, 6002]
    j5 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(max_credit(j1, j2, j3, j4, j5))
    j1 = [5000, 6500]
    j2 = [6000]
    j3 = [6500]
    j4 = [6000]
    j5 = [0, 5800, 6000]
    print(max_credit(j1, j2, j3, j4, j5))

if __name__ == '__main__':
    main()


