# 2020/01/28 ✔️

## Question
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array `[10, 5, 7]`, you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array `[10, 5, 1]`, you should return false, since we can't modify any one element to get a non-decreasing array.

## Proposed Solution
Take by threes starting with the very first element and change the numbers when necessary, keeping track of how many changes have been done.

Could shortcircuit as soon as more than one number needs to change but it's nice to see the entire resulting array in the end so I left that in.

## Testing
CLI will ask for the numbers in the sequence in order, ending with -1. Will print the resulting non-decreasing array and then `True` or `False` depending on whether the original sequence can become non-decreasing with at most one change or not.
