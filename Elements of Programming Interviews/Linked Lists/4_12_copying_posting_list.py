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

    def __str__(self):
        out = ''
        n = self.head
        while n is not None:
            out += str(n)
            n = n.next_node
        return out


test = PostingList('a')
test.add('b')
test.add('c')
test.add('d')
print(test)
