"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    single_skip_move = head
    double_skip_move = head
    while double_skip_move.next != None:
        double_skip_move = double_skip_move.next
        if single_skip_move == double_skip_move:
            return True
        double_skip_move = double_skip_move.next
        single_skip_move = single_skip_move.next
    return False


if __name__ == '__main__':
    head = None
    if has_cycle(head):
        print('1')
    else:
        print('0')
