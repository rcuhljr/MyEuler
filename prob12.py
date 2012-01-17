import myprimes
import cProfile
import math
from itertools import count

memo = {1:1}

memprime = {1:2}

def memPrime(primes, x):
    if not x in memprime:
        memprime[x] = primes.prime(x)
    return memprime[x]

def trinum(n):
    if not n in memo:
        memo[n] = trinum(n-1)+n
    return memo[n]  

def countFactors(n):
    return 2+sum(map(lambda x: 1 if n%x == 0 else 0, range(2,n)))
    
def solve(target):    
    triangles = ( trinum(i) for i in count() if i > 0)    
    skip = False
    for n in triangles:    
        if countFactors(n) > target:
            print n
            break

def countFactors2(primes, n):         
    def fillPrimes(primes, n):
        count = 1
        result = []
        cutoff = n/2
        while True:
            val = memPrime(primes,count)
            if val > n:
                return result
            if n%val == 0:            
                result.append(val)
                n /= val
            count += 1     
        return result
        
    primelist = fillPrimes(primes, n)           
    def function(x):
        value = n
        result = 1
        while (value%x == 0):
            value /= x
            result += 1
        return result    
    return reduce(lambda a, b: a*b,map(function, primelist))    
    
def solve2(target):    
    primes = myprimes.Primes()
    triangles = ( trinum(i) for i in count() if i > 1)    
    skip = False
    for n in triangles:
        if n%2 == 1:
            continue
        lastDigit = int(str(n)[-1])
        if not (lastDigit == 0 or lastDigit == 6 or lastDigit == 8):
            continue
        result = countFactors2(primes, n)
        if  result > target:
            print n
            break
            
print cProfile.run('solve2(500)')

#Seems like it should be straightforward, loop adding natural numbers and on each call count the factors.
#And defeated by scaling, look into a faster way to find factors.