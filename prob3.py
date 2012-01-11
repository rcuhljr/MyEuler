import math
primes = [2]

def fillPrimesFor(x):
    map(pumpPrime, range(3,math.trunc(math.sqrt(x)),2))
    
def pumpPrime(x):
    for n in primes:
        if x%n == 0:
            return        
    primes.append(x)        
        
def solve(x):
    fillPrimesFor(x)
    biggestFactor = 0;
    for n in primes:
        if x%n == 0 and n > biggestFactor:
            biggestFactor = n
    print biggestFactor    


solve(600851475143)

#going to attempt to speed this up with a better prime seive.