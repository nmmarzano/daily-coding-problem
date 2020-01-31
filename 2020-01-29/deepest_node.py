class Tree:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}:{{{self.left},{self.right}}}'


def deepest_leaf(tree, base=0):
    count = base + 1
    if tree.left is None and tree.right is None:
        return [tree, count]
    else:
        if tree.left is not None and tree.right is not None:
            dl = deepest_leaf(tree.left, count)
            dr = deepest_leaf(tree.right, count)
            return dl if dl[1] > dr[1] else dr
        else:
            return deepest_leaf(tree.left, count) if tree.left is not None else deepest_leaf(tree.right, count)


if __name__ == '__main__':
    tree = Tree('a', Tree('b', Tree('d', None, Tree('e'))), Tree('c', Tree('f', None, Tree('g', Tree('h', None, Tree('i'))))))
    print(tree)
    print(deepest_leaf(tree))
