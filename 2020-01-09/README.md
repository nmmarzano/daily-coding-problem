# 2020/01/09 ✔️

## Question
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset `{15, 5, 20, 10, 35, 15, 10}`, it would return true, since we can split it up into `{15, 5, 10, 15, 10}` and `{20, 35}`, which both add up to `55`.

Given the multiset `{15, 5, 20, 10, 35}`, it would return false, since we can't split it up into two subsets that add up to the same sum.

## Proposed Solution
"Serialize" numbers in the case the "set" has duplicates, get all subsets, then for each subset calculate the difference with the original set, get the sum of the subset and the difference, and compare the sums.

## Testing
Interactive for CLI! It will ask for the numbers in the set, letting you finish the input by entering -1. It's the future!
