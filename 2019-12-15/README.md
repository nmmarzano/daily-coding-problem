# 2019/12/15 ✔️

## Question
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

## Proposed Solution
Python makes this super easy* so I also implemented a couple well-known sorts for practice, but they're all quadratic time.

Merge sort obviously does not comply with the restriction to only do in-place swaps.

*\* turns out it's in n\*log(n) time, so I'll have to come back to this one.*

### Actual Solution
Turned out to be easier than expected: we got three "stacks" of the same value so, for example, when a new 'R' is found it is swapped with whatever comes right after the stack of 'R's, and then whatever is found is swapped with what comes after the stack of 'G's. If a 'G' is found, only the top value of the stack of 'G's is swapped. When a 'B' is found nothing happens since it is already at the top of the stack of 'B's. This makes it so there's at most 2 swaps per iteration, making it run in O(N) time.

All swaps are in-place, but it takes a little extra memory to store the offsets for each value type.

The following is a sample run for illustration purposes:

    input: ['G', 'B', 'R', 'R', 'B', 'R', 'G']

    found G at position 0
	    swapping with top of G stack
	    ['G', 'B', 'R', 'R', 'B', 'R', 'G']

    found B at position 1
	    ['G', 'B', 'R', 'R', 'B', 'R', 'G']

    found R at position 2
	    swapping with top of R stack
	    ['R', 'B', 'G', 'R', 'B', 'R', 'G']
	    swapping with top of G stack
	    ['R', 'G', 'B', 'R', 'B', 'R', 'G']

    found R at position 3
	    swapping with top of R stack
	    ['R', 'R', 'B', 'G', 'B', 'R', 'G']
	    swapping with top of G stack
	    ['R', 'R', 'G', 'B', 'B', 'R', 'G']

    found B at position 4
	    ['R', 'R', 'G', 'B', 'B', 'R', 'G']
    
    found R at position 5
	    swapping with top of R stack
	    ['R', 'R', 'R', 'B', 'B', 'G', 'G']
	    swapping with top of G stack
	    ['R', 'R', 'R', 'G', 'B', 'B', 'G']

    found G at position 6
	    swapping with top of G stack
	    ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    Result: ['R', 'R', 'R', 'G', 'G', 'B', 'B']

## Testing
Asserts that the result is the same as that of the "batteries included" sort that runs in N\*log(N) time and prints the result if so. Otherwise it shows the array with an AssertionError message.
