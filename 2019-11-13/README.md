# 2019/11/13 ✔️

## Question
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following `Node` class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

## Proposed Solution
Trivial to implement with JSON serialization so a simple serialization by hand was tackled.

Ha ha man this sucks. Not proud of it, "it works" levels of quality. Super simple serializer, mess of a deserializer. Does allow for any character in the node values though so that's nice.

The python version is based on the solution found at https://dev.to/cwetanow/daily-coding-problem-3-73i and while the code is mine, I did not come up with the solution myself. Uses a root-first order not unlike my solution but takes advantage of it to deserialize through the use of a queue, which also allows for simpler serialization. Second year algorithms class! It's a heckton nicer to look at.

## Testing
Create instances of `SerialTree.Node`, build a tree, then apply `SerialTree.serialize(Node node)` and `SerialTree.deserialize(String s)` to your heart's content.
