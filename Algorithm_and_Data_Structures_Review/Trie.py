import unittest


class TrieNode:
    def __init__(self, data):
        self.data = ''
        self.siblings = dict()
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def add(self, word):
        cur_node = self.root
        for letter in word:
            if letter in cur_node.siblings:
                cur_node = cur_node.siblings[letter]
            else:
                temp = TrieNode(letter)
                cur_node.siblings[letter] = temp
                cur_node = temp
        cur_node.isWord = True

    def is_prefix(self, prefix, start=None):
        cur_node = start if start else self.root
        for letter in prefix:
            if letter in cur_node.siblings:
                cur_node = cur_node.siblings[letter]
            else:
                return False
        return cur_node

    def is_word(self, word):
        cur_node = self.root
        for letter in word:
            if letter in cur_node.siblings:
                cur_node = cur_node.siblings[letter]
            else:
                return False
        if cur_node.isWord:
            return True
        return False

    def remove_word(self, word):
        cur_node = self.root
        for letter in word:
            if letter in cur_node.siblings:
                cur_node = cur_node.siblings[letter]
            else:
                return False
        cur_node.isWord = False


class MyTestCases(unittest.TestCase):
    def test_Trie(self):
        test = 'test'
        trie = Trie()
        trie.add(test)
        self.assertTrue(trie.is_word('test'))
        self.assertTrue(trie.is_prefix('t'))
        self.assertTrue(trie.is_prefix('te'))
        self.assertTrue(trie.is_prefix('tes'))
        self.assertTrue(trie.is_prefix('test'))
        self.assertFalse(trie.is_word('tes'))
        self.assertFalse(trie.is_prefix('a'))
        self.assertFalse(trie.is_prefix('ta'))
        self.assertFalse(trie.is_prefix('tests'))
        self.assertFalse(trie.is_prefix('tesa'))
        trie.add('tests')
        self.assertTrue(trie.is_prefix('tests'))
        self.assertTrue(trie.is_word('tests'))
        self.assertTrue(trie.is_word('test'))
        trie.remove_word('test')
        self.assertFalse(trie.is_word('test'))
        self.assertTrue(trie.is_word('tests'))