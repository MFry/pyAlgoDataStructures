"""
    Difficulty: ***
    Code:       ***
The awards committee had planned to give n research grants this year, out of a its total yearly budget.
However, the budget was reduced to b dollars.
The committee members has decided to affect the minimal number of highest grants,
 by applying a maximum cap c on all grants: every grant that was planned to be higher than c will now be c dollars.
Help the committee to choose the right value of c that would make the total sum of grants equal to the new budget.

Given an array of grants g and a new budget b, explain and code an efficient method to find the cap c.
 Assume that each grant is unique.
Analyze the time and space complexity of your solution.


"""


def award_budget(p_budget, b):
    p_budget.sort()
    current_budget = sum(p_budget)
    min_change = 0
    max_cap = 0
    for i in range(len(p_budget) - 1, -1, -1):
        if current_budget > b:
            leftover = b - current_budget
            leftover /= min_change
            if leftover > p_budget[i]:
                return leftover
        current_budget -= p_budget[i]
        min_change += 1
    return max_cap
