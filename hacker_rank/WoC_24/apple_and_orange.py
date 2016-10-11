"""

"""


def main():
    s, t = [int(i) for i in input().split()]
    a, b = [int(i) for i in input().split()]
    _ = input()
    apples = [int(i) for i in input().split()]
    oranges = [int(i) for i in input().split()]
    a_fallen, o_fallen = 0, 0
    for apple in apples:
        if s <= apple + a <= t:
            a_fallen += 1
    for orange in oranges:
        if s <= orange + b <= t:
            o_fallen += 1
    print(a_fallen)
    print(o_fallen)


if __name__ == '__main__':
    main()
