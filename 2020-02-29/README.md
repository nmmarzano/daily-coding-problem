# 2020/02/29 ✔️

## Question

Given a word `W` and a string `S`, find all starting indices in `S` which are anagrams of `W`.

For example, given that `W` is `"ab"`, and `S` is `"abxaba"`, return 0, 3, and 4.

## Proposed Solution

Start by sorting `W`, then iterate over `S`, taking every string with the same length as `W`, sorting it, and comparing it to the sorted `W`. If the strings are equal, add the current index to the return values.

## Testing

Running the program will first ask for W, then for S, and then it will print the list of indices.
