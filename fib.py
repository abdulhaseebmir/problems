# normal implementation
def fib_normal(n):
    if n <= 2:
        return 1

    return fib_normal(n-1) + fib_normal(n-2)


# print(fib_normal(6))
# print(fib_normal(7))
# print(fib_normal(8))


# memoization
def fib(n, memo={}):
    
    # see if we can reuse something
    if n in memo:
        return memo[n]
    
    if n<=2:
        return 1
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    print(memo)
    return memo[n]

print(fib(6))
