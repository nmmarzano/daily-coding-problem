# 2020/01/31 ✔️

## Question
Using a `read7()` method that returns 7 characters from a file, implement `readN(n)` which reads `n` characters.

For example, given a file with the content `“Hello world”`, three `read7()` returns `“Hello w”`, `“orld”` and then `“”`.

## Proposed Solution
Keep a buffer of "exceeding characters", read from buffer first, then call `read7()` as many times as necessary, leaving all exceeding characters in there for the next read.
    
## Testing
Running the code will first show `read7()` working as expected, and then ask for the number of characters to read using `readN()`. Ends on entering `99`.
