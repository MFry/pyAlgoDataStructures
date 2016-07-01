import unittest
import linkedlist


class PostingList(linkedlist.LinkedList):

    class PostingNode(linkedlist.Node):

        def __init__(self, value, posting=None):
            """

            :param value:
            :param posting:
            :type posting: PostingNode
            """
            linkedlist.Node.__init__(self, value)
            self._posting_node = posting

        @property
        def posting(self):
            return self._posting_node

        @posting.setter
        def posting(self, post_node):
            self._posting_node = post_node

        def __str__(self):
            if self.posting:
                post_value = self.posting.value
            else:
                post_value = self.posting
            return '[Val]' + str(self.value) + '[Post]' + str(post_value) + ' - '

    def add(self, val=None, node=None, post_node=None):
        if val:
            n = PostingList.PostingNode(val, post_node)
        elif node:
            n = node
        linkedlist.LinkedList.add(self, node=n)

    def _find_node(self, val):
        n = self.head
        while n is not None:
            if n.value == val:
                return n
            n = n.next_node
        return None

    def set_connection(self, start, end=None):
        n = self._find_node(start)
        connection = self._find_node(end)
        n.posting = connection

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        n = self._current
        self._current = self._current.next_node
        return n

    def __str__(self):
        out = ''
        n = self.head
        while n is not None:
            out += str(n)
            n = n.next_node
        return out


def copy_posting_list(posting_list):
    """
    Copy function that takes O(n) time and O(1) space

    :param posting_list:
     :type posting_list: PostingList
    :return:
     :rtype: PostingList
    """
    post_copy = PostingList()
    for node in posting_list:
        post_copy.add(val=node.value)

    org_node = posting_list.head
    copy_node = post_copy.head

    while org_node and copy_node:
        org_next = org_node.next_node
        copy_next = copy_node.next_node

        org_node.next_node = copy_node
        copy_node.next_node = org_next

        org_node = org_next
        copy_node = copy_next

    return posting_list


class MyTestCase(unittest.TestCase):
    def setUp(self):
        test = PostingList('a')
        test.add('b')
        test.add('c')
        test.set_connection('a', 'c')
        test.add('d')
        test.set_connection('b', 'd')
        test.set_connection('c', 'b')
        test.set_connection('d', 'd')
        self.posting_list = test

    def test_PostingList(self):
        test = self.posting_list
        print(test)

    def test_copy(self):
        test = self.posting_list
        print(copy_posting_list(test))

if __name__ == '__main__':
    unittest.main()
