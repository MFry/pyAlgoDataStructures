"""

"""
import unittest


def quick_partition(arr, partition_index):
    left = []
    right = []
    equal = []
    for i in range(len(arr)):
        if arr[i] < arr[partition_index]:
            left.append(arr[i])
        elif arr[i] > arr[partition_index]:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    return left + equal + right


def main():
    t = int(input())
    arr = [int(i) for i in input().split()]
    print(' '.join([str(i) for i in quick_partition(arr, 0)]))


if __name__ == '__main__':
    main()
