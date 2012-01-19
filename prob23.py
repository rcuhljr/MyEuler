import math
import cProfile
import myprimes

def generate_abundants():
    primes = myprimes.Primes()
    result = {}
    for n in range(2,28124):                
        if sum(primes.proper_divisors(n)) > n:
            result[n] = 0
    return result    

def solve():    
    ab_numbers = generate_abundants()
    
    def fast_in(n):
        count = 0
        while ab_numbers[count] <= n:
            if ab_numbers[count] == n:
                return True
            count += 1
        return False    
    
    def function(n):     
        for x,v in ab_numbers.iteritems():            
            if x > n:                
                return n
            if ab_numbers.has_key(n-x):
                return 0                    
    print sum(map( function, range(1,28124)))
    
print cProfile.run('solve()')

#started caching divisors, because this is coming up a lot and it still takes me 30~ seconds
#to generate all divisors for 1-20000