# 2020/02/16 ✔️

## Question
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

`exists(board, "ABCCED")` returns `true`,

`exists(board, "SEE")` returns `true`,

`exists(board, "ABCB")` returns `false`.

## Proposed Solution
Iterate over the board, erasing the letter from the word if a match is found, return true if the word is now empty (meaning all letters were found in the board).
    
## Testing
Running the code shows the result of running the three tests included in the question.
