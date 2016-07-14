"""
 Problem 11
 Data Structures : Trie, Bloom Filters
"""
import unittest


class UrlEncodingUsingTrie:
    def __init__(self):
        self._visited_paths = {}

    @property
    def visited(self):
        return self._visited_paths

    @visited.setter
    def visited(self, link):
        """

        :param link:
        :type link: str
        :return:
        """
        link = list(link)
        trie_node = self._visited_paths
        for character in link:
            if character in trie_node:
                trie_node = trie_node[character]
            else:
                trie_node[character] = {}
                trie_node = trie_node[character]
        trie_node[link[-1]] = {'*': True}


# TODO : Bloom Filters with run length encoding
class MyTestCase(unittest.TestCase):
    def test_UrlEncodingUsingTrie(self):
        test_link = 'www.a.co'
        encoding = UrlEncodingUsingTrie()
        encoding.visited = test_link
        test_link = 'www.alpha.com'
        encoding.visited = test_link
