import math
import cProfile
import myprimes
   
def count_primes(a, b, primes):    
    for i in range(100):
        if not primes.is_prime(i**2+a*i+b):
            return i
   
def solve(amax, bmax):    
    primes = myprimes.Primes()
    max = (0, 0, 0)
    for a in range(-1*amax+1, amax):
        for b in range(-1*bmax+1, bmax):            
            numPrimes = count_primes(a, b, primes)            
            if numPrimes > max[0]:
                max = (numPrimes, a, b)
    print max   
    
print cProfile.run('solve(1000,1000)')

#brute force, go!