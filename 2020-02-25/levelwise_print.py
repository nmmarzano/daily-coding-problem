from tree import Tree


def levelwise_print(t):
    nodes = [t]

    while len(nodes) > 0:
        node = nodes[0]
        print(node.val)
        if node.left is not None:
            nodes.append(node.left)
        if node.right is not None:
            nodes.append(node.right)
        nodes = nodes[1:]


if __name__ == '__main__':
    tree = Tree(1, Tree(2), Tree(3, Tree(4), Tree(5)))
    levelwise_print(tree)
