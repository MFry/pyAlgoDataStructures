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
            linkedlist.Node.__init__(value)
            self._posting_node = posting

        @property
        def posting(self):
            return self._posting_node

        @posting.setter
        def posting(self, post_node):
            self._posting_node = post_node

        def __str__(self):
            return '[Val]'+str(self.value)+'[Post]'+str(self.posting.value) +' -'

    def add(self, val=None, node=None, post_node=None):
        if val:
            n = PostingList.PostingNode(val, post_node)
        elif node:
            n = node
        linkedlist.LinkedList._add(node=n)



test = PostingList('a')
test.add('b')
test.add('c')
test.add('d')
