import math
import cProfile
primes = [2]
    
def pumpPrime(x):
    cutoff = math.sqrt(x)
    for n in primes:
        if x%n == 0:
            return 
        elif n > cutoff:
            break
    primes.append(x)        
        
def solve(x):
    count = 3
    while len(primes) < x:
        pumpPrime(count)
        count += 2
    print primes[len(primes)-1]

print cProfile.run('solve(10001)')

#yay code reuse