'''
Based on the version found at:
https://dev.to/cwetanow/daily-coding-problem-3-73i

Does not allow for the use of the empty or append markers,
and will fail to deserialize a tree with nodes containing them
in their values.

Serializes the tree in root-first order.
Uses the root-first values as a queue to deserialize the tree.
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


EMPTY_MARKER = '*'
APPEND_MARKER = '-'

def serialize(node):
    if EMPTY_MARKER in node.val or APPEND_MARKER in node.val:
        return ''
    
    result = []
    if node == None:
        result.append(EMPTY_MARKER)
        result.append(APPEND_MARKER)
    else:
        result.append(node.val)
        result.append(APPEND_MARKER)
        result.append(serialize(node.left))
        result.append(serialize(node.right))
    
    return ''.join(result)


def deserialize(tree_str):
    queue = tree_str.split(APPEND_MARKER)[:-1]
    return deserialize_node(queue)[0]


def deserialize_node(queue):
    print(queue)
    if queue[0] != EMPTY_MARKER:
        node = Node(queue[0])
        queue = queue[1:]
        node.left, queue = deserialize_node(queue)
        node.right, queue = deserialize_node(queue)
    else:
        queue = queue[1:]
        node = Node(None)
    return [node, queue]
