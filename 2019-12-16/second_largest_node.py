class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def size(tree):
    if tree == None:
        return 0
    else:
        #return 1 + size(tree.left) + size(tree.right)
        return tree.val + size(tree.left) + size(tree.right)

def second_largest_node(tree):
    return tree.left if size(tree.left) > size(tree.right) else tree.right


if __name__ == '__main__':
    tree = Node(1, Node(2, Node(3), Node(4)), Node(5))
    sln = second_largest_node(tree)
    print('tree: Node(1, Node(2, Node(3), Node(4)), Node(5))')
    print('SLN: size: {}, value of root: {}'.format(size(sln), sln.val))
    tree = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7, Node(8))))
    sln = second_largest_node(tree)
    print('tree: Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7, Node(8))))')
    print('SLN: size: {}, value of root: {}'.format(size(sln), sln.val))
