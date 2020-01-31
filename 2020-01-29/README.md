# 2020/01/29 ✔️

## Question
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

        a
       / \
      b   c
     /
    d


## Proposed Solution
Recursive solution: start at depth 0. If the current node has no children, return it together with depth+1. If it does, between calling deepest_leaf on the left and right children, return the one that has the greater depth.
    
## Testing
Running the code will print a test tree and then print the deepest node in the tree.
