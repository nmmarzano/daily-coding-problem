# 2020/01/23 ✔️

## Question

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

      1
     / \
    2   3
       / \
      4   5

## Proposed Solution

Push the root of the tree into a list.

For every element in the list, print its value, push the left and right elements into the list, and then delete it from the list.

In this way, all the values are pushed into the list, and printed, level-wise; all the elements of the next level will be pushed after all the elements of the current level.
    
## Testing

Running the program will show the level-wise print of the example tree.
