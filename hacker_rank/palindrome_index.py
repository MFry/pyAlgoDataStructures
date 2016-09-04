"""
    Ref: https://www.hackerrank.com/challenges/palindrome-index
"""


def is_palindrome(to_check, start, end):
    while start < end:
        if to_check[start] != to_check[end]:
            return False
        start += 1
        end -= 1
    return True


def palindrome_creation(letters):
    start = 0
    end = len(letters) - (1 + start)
    while start < end:
        end = len(letters) - (1 + start)
        if letters[start] == letters[end]:
            start += 1
            continue
        if is_palindrome(letters, start + 1, end):
            return start
        else:
            return end

    return -1


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        print(palindrome_creation(input()))
