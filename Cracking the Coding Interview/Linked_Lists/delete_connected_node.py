import unittest


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __bool__(self):
        return bool(self.data)


def delete_connected_node(to_remove):
    if not to_remove or not to_remove.next:
        raise Exception('Invalid node {}'.format(to_remove))
    next_node = to_remove.next.next
    to_remove.data = to_remove.next.data
    to_remove.next = next_node


class MyTestCases(unittest.TestCase):

    def test_delete(self):
        test1 = Node('a')
        test1.next = Node('b')
        test1.next.next = Node('c')
        correct_next = test1.next.next
        to_del = test1.next
        delete_connected_node(to_del)
        self.assertEqual(test1.next.data, correct_next.data)