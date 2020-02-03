class Tree:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}:{{{self.left},{self.right}}}'


def invert_tree(tree):
    if tree is not None:
        invert_tree(tree.left)
        invert_tree(tree.right)
        aux = tree.left
        tree.left = tree.right
        tree.right = aux


if __name__ == '__main__':
    tree = Tree('a', Tree('b', Tree('d'), Tree('e')), Tree('c', Tree('f')))
    print(tree)
    invert_tree(tree)
    print(tree)
