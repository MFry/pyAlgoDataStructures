class Node:
    def __init__(self, value):
        self._value = value
        self._next_node = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class LinkedList:

    def __init__(self, val=None):
        if val:
            self._set_first(val)
        else:
            self._head = None
            self._tail = None
            self._length = 0

    def _set_first(self, val):
        self._head = Node(val)
        self._tail = self._head
        self._length = 1

    @property
    def tail(self):
        """

        :return: Returns the last node in the linked list
        :rtype: Node
        """
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    @property
    def head(self):
        """

        :return: Linked List Starting Value
        :rtype: Node
        """
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def add(self, val):
        n = Node(val)
        if not self.head:
            self._set_first(val)
        else:
            self.tail.next_node = n
            self.tail = n
            self._length += 1

    def __len__(self):
        return self._length


def reverse_list(linked_list):
    current_node = linked_list.head
    prev_node = None
    while current_node is not None:
        t = current_node.next_node
        current_node.next_node = prev_node
        current_node, prev_node = t, current_node
    linked_list.head = prev_node
    return linked_list


def main():
    empty = LinkedList()
    print('LinkedList is empty', len(empty) == 0)
    one_node = LinkedList(2)
    print('Head and tail match and length is 1', one_node.head == one_node.tail and len(one_node) == 1)
    several_nodes = LinkedList()
    several_nodes.add(1)
    several_nodes.add(2)
    several_nodes.add(3)
    several_nodes.add(4)
    print('Length is 4', len(several_nodes) == 4)
    n = several_nodes.head
    while n is not None:
        print('Node val:', n.value)
        n = n.next_node
    reverse_list(several_nodes)
    n = several_nodes.head
    while n is not None:
        print('Node val:', n.value)
        n = n.next_node


if __name__ == '__main__':
    main()
