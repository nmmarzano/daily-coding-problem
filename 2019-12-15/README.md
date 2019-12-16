# 2019/12/15 

## Question
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

## Proposed Solution
Python makes this super easy* so I also implemented a couple well-known sorts for practice, but they're all quadratic time.

Merge sort obviously does not comply with the restriction to only do in-place swaps.

*\* turns out it's in n\*log(n) time, so I'll have to come back to this one.*

## Testing
Prints the outputs for each sort
