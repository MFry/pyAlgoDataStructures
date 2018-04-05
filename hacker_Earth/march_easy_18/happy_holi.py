"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""


# Write your code here
def min_treats_to_traverse(path, start, end):
    # start -> end
    min_candy, path_cost = float('inf'), 0
    current = path[start]
    for i in range(min(start, end), max(start, end)):
        if current != path[i]:
            path_cost += 1
            current = path[i]
    min_candy = min(min_candy, path_cost)
    current, path_cost = path[start], 0
    # end <- start
    for i in range(abs(end - start)):
        if current != path[start - i]:
            path_cost += 1
            current = path[i]
    min_candy = min(min_candy, path_cost)
    return min_candy


def driver():
    from sys import stdin, stdout
    test_cases = int(input())
    for _ in range(test_cases):
        __, paths = [int(i) for i in input().split()]
        path = [i for i in input()]
        for ___ in range(paths):
            start, end = [int(i) for i in input().split()]
            print(min_treats_to_traverse(path, start - 1, end - 1))


if __name__ == '__main__':
    with open('113b734802-in09.txt') as f:
        test_cases = int(f.readline())
        data = f.readlines()
        for _ in range(test_cases):
            print('N,Q:', data[0])
            __, lines = [int(i) for i in data[0].split()]
            data.pop(0)
            path = [i for i in data.pop(0)]
            for i in range(lines):
                start, end = [int(j) for j in data[i].split()]
                print(min_treats_to_traverse(path, start - 1, end - 1))
            print('data line 100', data[100])
            print('Lines completed', lines, 'input size', len(data))

            data = data[lines:]
            print('data sliced', data)


