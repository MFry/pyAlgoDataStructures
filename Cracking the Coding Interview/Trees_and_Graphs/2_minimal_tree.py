class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_shortest_minimal_bst(arr):
    mid_point = -(-len(arr)//2)
    root = Node(arr[mid_point])
    create_shortest_sub_bst(root, arr, 0, mid_point-1)
    create_shortest_sub_bst(root, arr, mid_point+1, len(arr)-1)


def create_shortest_sub_bst(root, arr, start, stop):
    # base case
    if stop - start < 0:
        return
    mid_point = -(-len(arr)//2)
    leaf = arr[mid_point]
    attach_node(root, leaf)
    create_shortest_sub_bst(leaf, arr, start, mid_point-1)
    create_shortest_sub_bst(leaf, arr, mid_point+1, stop)


def attach_node(root, child):
    if root.data <= child:
        root.left = child
    else:
        root.right = child
