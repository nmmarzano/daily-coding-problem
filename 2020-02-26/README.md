# 2020/02/26 ✔️

## Question

Given a function `f`, and `N` return a debounced `f` of `N` milliseconds.

That is, as long as the debounced `f` continues to be invoked, `f` itself will not be called for `N` milliseconds.

## Proposed Solution

Standard solution derived from [my js gist](https://gist.github.com/nmmarzano/85feabf59f3f6986a9e6ba31ad2a2790).
    
## Testing

Running the program shows how trying to call the debounced function constantly and rapidly only results in a handful of calls to the actual function.
