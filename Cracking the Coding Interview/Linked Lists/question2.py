"""
Algorithm that finds kth to last element in a singly linked list
"""
from linkedlist import LinkedList


def findKelementh(list, k):
    """

    :param list:
    :type list: LinkedList
    :param k:
    :type k: int
    :return:
    """
    i = 0
    node = list.head
    kth_node = None
    while node is not None:
        # We could check if the list is circular so we don't get stuck in an infinite loop
        node = node.next_node
        if kth_node:
            kth_node = kth_node.next_node
        else:
            i += 1
            if i == k:
                kth_node = list.head

    return kth_node


def main():
    test = LinkedList()
    for i in range(20):
        test.add(i)
    print(test)
    print('Find the node before last', findKelementh(test, 2))
    print('Find the last node', findKelementh(test, 1))
    print('Finding 12th to last Node: ', findKelementh(test, 12))

if __name__ == '__main__':
    main()
