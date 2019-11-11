# Sample Programming Interview Question

## Question
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

 - 1, 1, 1, 1
 - 2, 1, 1
 - 1, 2, 1
 - 1, 1, 2
 - 2, 2
 
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

## Proposed Solution
Imagining the paths as a tree of possibilities gave me the idea to solve it in a recursive way. The printing inside the function is not pretty but it works for debugging and it's just nice to visualize the found paths, so I left it in.

## Testing
The function `Staircase.waysToClimb(int steps, int[] alts)` takes the total number of steps in the staircase and an array with the different amount of steps you can take at a time, and returns the unique number of ways you can climb the stairs as an integer. It also prints the different paths by itself.
