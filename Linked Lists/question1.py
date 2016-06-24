"""
    Remove duplicate nodes from an unordered linked list
"""
import linkedlist


def remove_duplicates(list):
    if not list:
        return None

    prev = list.head
    n = list.head
    values_found = {}
    while n:

        if n.value in values_found:
            prev.next_node = n.next_node
            n = prev
        else:
            values_found[n.value] = True
        prev = n
        n = n.next_node
    return list


List = linkedlist.LinkedList
test = List(5)
test.add(5)
test.add(5)
test.add(5)
print(remove_duplicates(test))
print(remove_duplicates(test))
test = List(342)
for i in range(10):
    test.add(i)
print(remove_duplicates(test))
for i in range(25):
    test.add(i)
print(remove_duplicates(test))
test.add(24)
test.add(342)
print(remove_duplicates(test))
