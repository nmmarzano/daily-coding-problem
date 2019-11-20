# 2019/11/12 ✔️

## Question
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

## Proposed Solution
One pass to calculate the total product, one pass to fill up the array with a single division.

O(N), but it can't handle having a zero, since it will result in dividing by zero.

The version without division can handle zeroes but it turns it up to O(N^2).

## Testing
`ExclusiveProduct.calculate(int[] numbers)` takes an array of numbers and returns the resulting array.
