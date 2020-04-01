# 2020/04/01 ✔️

## Question
Given a pivot `x`, and a list `lst`, partition the list into three parts.

The first part contains all elements in `lst` that are less than `x`
The second part contains all elements in `lst` that are equal to `x`
The third part contains all elements in `lst` that are larger than `x`
Ordering within a part can be arbitrary.

For example, given `x = 10` and `lst = [9, 12, 3, 5, 14, 10, 10]`, one partition may be `[9, 3, 5, 10, 10, 12, 14]`.

## Proposed Solution
Two solutions provided: one simply iterates over the list, copies every number into a different list depending on if the number is lesser than, equal to, or greater than the pivot, and then returns the joined lists.

The other solution is a little more complicated and solves the pivot sorting in-place.
The pivot is searched for in the list, then everything on the left that's bigger than it is thrown to the right and vice-versa.
Numbers equal to the pivot are moved next to it.
    
## Testing
Running the code will show a prompt asking for a pivot and show the results of both algorithms. For the sake of testing, a more complete example list is coded in.
