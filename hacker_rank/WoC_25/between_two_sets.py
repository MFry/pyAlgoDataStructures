"""

1) Compute the Lowest Common Multiple (LCM) of A.
2) Compute the Greatest Common Divisor (GCD) of B.
If x is 'between' A and B, then it will be a multiple of LCM(A) and a divisor of GCD(B). So we can now check any value x without having to step through A and B.
3)If LCM(A) is not a factor of GCD(B), then no x can be 'between' A and B so we just print 0 and quit.
4) If LCM(A) is a factor of GCD(B), then the number of multiples of LCM(A) that are factors of GCD(B) is the same as the number of integer factors of GCD(B) / LCM(A). So the problem is now reduced to integer factorisation.
While the simple approach won't work for 50 digit numbers(but still fast enough for a 64 bit number if we stop at the squre root), there are a lot of really clever algorithms like the Quadratic Sieve and Lenstras' Elliptic Curve Method that are really fast. I'm not entirely sure how they work, but I have copy pasted code into my IDE and tried them out, it is indeed possible to factorise 50 digit numbers without timing out on HackerRank.
-8  | Add Comment Parent Permalink


Bad_Jim about 6 hours ago
This is more for the hypothetical scenario where the constraints are much higher and everything has to be done with maximum efficiency. If you simply want your 10 points, the easiest thing to do is ignore all these optimizations and write a brute force solution.
0   | Add Comment Parent Permalink

hacker_am1xh53a about 5 hours ago
For higher constraints it does not look very efficient, as calculating LCM(A) is very expensive, say, if A are up to 10^17, N and M up to 10^6, LCM(A) might be of 16 million digits, and calculating it straightforward way would cost about 10^12 operations.
Though it is possible to stop calculations when LCM become larger than the limit for Bi, it wouldrequire more accurate calculations, probably of higher precision. LCM calculation is better replaced with calculation of some GCD.
And in the end we might stop at cubic instead of square root if we check the remainder for primality, because we do not need exact factors, only their count and multiplicity.
0   | Add Comment Parent Permalink

Bad_Jim about 3 hours ago
LCM(A) probably isn't the issue. If it gets larger than GCD(B) then we just print zero and stop. And we can calculate the LCM like this:
LCM(y,z) = y*z / GCD(y,z)
So LCM is a little bit more complicated than GCD, but the calculation of GCD(B) necessarily deals with larger numbers. Though it is possible that B might have far less values than A.
I like the idea of going up to the cube root, but modern factorisation techniques are still much faster. However they aren't systematic searches like trial division in the sense that you can say all factors below the cube root have been found. You just keep finding factors and testing primality until you run out of composite numbers.

Ref:
"""
import unittest


def common_factors_of_set(s, factors=set()):
    factors = set(factors)
    # find all factors for the smallest s
    to_factor = min(s)
    for i in range(1, to_factor + 1):
        if to_factor % i == 0:
            factors.add(i)
    s.remove(to_factor)
    for num in s:
        to_remove = set()
        for factor in factors:
            if num % factor != 0:
                to_remove.add(factor)
        factors = factors.difference(to_remove)
    return factors


class MyTestCases(unittest.TestCase):
    def test_common_factors_of_set(self):
        factors = common_factors_of_set([16, 32, 96])
        print(common_factors_of_set(factors, [2, 4]))
