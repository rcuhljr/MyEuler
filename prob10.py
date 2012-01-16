import math
import cProfile
import myprimes
   
def solve(target):
    primes = myprimes.Primes()
    sum = 0
    count = 1
    while primes.prime(count)<target:               
        sum += primes.prime(count)
        count += 1
    print sum

print cProfile.run('solve(2000000)')

#made a slightly more vibrant primes class since this seems like it will be a theme.