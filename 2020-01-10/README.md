# 2020/01/10 ✔️

## Question
Implement integer exponentiation. That is, implement the `pow(x, y)` function, where `x` and `y` are integers and returns `x^y`.

Do this faster than the naive method of repeated multiplication.

## Proposed Solution
Calculates 10^100000 in 0.050s as opposed to the 1.569s of the naive method.

Done by "grouping" factors by pairs, doing log2(y) passes. Visualization:

    2^5
    
    2 * 2 * 2 * 2 * 2
    
    (2 * 2) * (2 * 2) * 2
    
    4 * 4 * 2
    
    (4 * 4) * 2
    
    16 * 2
    
    32
    
I don't have to redo the calculation for each group, so I only do one calculation for the "group result" and then another to account for the leftover term in case there's an odd number of them. So for each step of the example above the calculation done goes like:

    // setup
    rest = 1; result = x = 2;
    // iteration 1
    rest = rest * result = 1 * 2 = 2; result = result * result = 2 * 2 = 4;
    // iteration 2
    result = result * result = 4 * 4 = 16;
    // post iterations
    result = result * rest = 16 * 2 = 32;
    
I've tried grouping them in groups of three but the end result has slightly worse performance due to the extra checks, making me think this might be the best version, though I haven't checked with bigger "groups".
    

## Testing
CLI interface will ask for x and y, then proceed to calculate x^y with both methods and show the times.
