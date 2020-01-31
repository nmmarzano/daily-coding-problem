# 2020/01/30 ✔️

## Question
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if `{“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}` then `“23”` should return `[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"]`.

## Proposed Solution
Pretty straightforward, just a double loop to combine every char of the first sequence with every char of the second.

## Testing
CLI will ask for the two number string and print the resulting list of combinations.
