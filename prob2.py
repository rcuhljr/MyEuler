memo = {0:1, 1:2}

def fib(x):
    if not x in memo:
        memo[x] = fib(x-1)+fib(x-2)
    return memo[x]    

def solve():
    
    def f(x):
        if x%2 == 0:
            return x
        else:
            return 0
    counter = 0
    result = 0

    while fib(counter) < 4000000:
        result += f(fib(counter))
        counter += 1    
    print result
    
solve()
    
#A little slower running then I'd like, wonder if caching is working properly.
#Caching is working fine, problem is actually that I'm calling fib, not mfib, redoing in file memoization.
# probably about 15-20 minutes to get memoization working and optimizing %2 problem.