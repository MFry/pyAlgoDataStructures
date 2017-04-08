import unittest


class Trie:

    def __init__(self):
        self._root = Node()

    def add(self, string):
        current_node = self._root
        for c in string:
            current_node = current_node.add_node(c)
        current_node.add_node(None)

    def find_count(self, string):
        current_node = self._root
        for c in string:
            if c in current_node.nodes:
                current_node = current_node.nodes[c]
            else:
                return 0
        return current_node.count


class Node:
    def __init__(self, value=None):
        self.nodes = {}
        self.parent = None
        self.count = 0
        self.value = value

    def __contains__(self, item):
        return item in self.nodes

    def add_node(self, val):
        self.count += 1
        if val not in self.nodes:
            new_node = Node(val)
            new_node.parent = self
            self.nodes[val] = new_node
        else:
            new_node = self.nodes[val]
        return new_node


class MyTestCases(unittest.TestCase):

    def test_tries_test(self):
        contacts = Trie()
        with open('tries_test.txt') as file:
            n = int(file.readline())
            for _ in range(n):
                op, contact = file.readline().strip().split(' ')
                if op == 'add':
                    contacts.add(contact)
                elif op == 'find':
                    print(contacts.find_count(contact))


if __name__ == '__main__':
    contacts = Trie()
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op == 'add':
            contacts.add(contact)
        elif op == 'find':
            print(contacts.find_count(contact))
