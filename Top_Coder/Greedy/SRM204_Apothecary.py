"""
    https://community.topcoder.com/stat?c=problem_statement&pm=2420&rd=5850

    Hint: Try to generalize this observation:

    Consider, for example, the 1-grain weight. Notice that the other weights are multiples of 3, so any combination of
     the other weights will yield a net result that is a multiple of three. If your target weight is not a multiple of
     three, then the 1-grain weight must be involved. If the target weight mod 3 is 1, then the 1-grain weight goes in
      the opposite pan. If the target weight mod 3 is 2, then the 1-grain weight goes in the same pan as the object.
      If the target weight mod 3 is 0, then the 1-grain weight is not used at all, because combining the 1-grain weight
       with other weights could never yield a multiple of three.
"""


def balance(w):
    weights = []
    current_weight = 1
    while w > 0:
        if w % 3 == 1:
            w -= 1
            # we place it as a counter balance
            weights.append(current_weight)
        elif w % 3 == 2:
            w += 1
            # place it with the weighted object
            weights.append(-1 * current_weight)
        w //= 3
        current_weight *= 3
    return sorted(weights)


def main():
    sol = [-9, -1, 27]
    print('Test case 1:', balance(17) == sol)
    sol = [1]
    print('Test case 2:', balance(1) == sol)
    sol = [-243, -9, 81, 2187]
    print('Test case 3:', balance(2016) == sol)
    sol = [-531441, -59049, -6561, -243, -27, 1, 81, 729, 2187, 1594323]
    print('Test case 4:', balance(1000000) == sol)


if __name__ == '__main__':
    main()
