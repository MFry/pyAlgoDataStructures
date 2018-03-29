"""
 Type: Dynamic programming
"""


# code
def maximum_nonadjacent_value(houses):
    max_value_at_location = [0 for _ in range(len(houses))]
    print(max_value_at_location)
    max_value_at_location[0], max_value_at_location[1] = houses[0], houses[1]
    for i in range(3, len(houses)):
        cur = houses[i]
        max_value_at_location[i] = max(cur + max_value_at_location[i - 1], cur + max_value_at_location[i - 2])
    return max_value_at_location[-1]


def driver(test_cases):
    for _ in range(test_cases):
        size = int(input())
        test_array = [int(i) for i in range(len(size))]
        print(size, test_array)
        print(maximum_nonadjacent_value(test_array))

