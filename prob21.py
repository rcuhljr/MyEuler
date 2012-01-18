import myprimes
import cProfile
import math
from itertools import count

tested_items = {0:-1,1:0}


def sum_proper_factors(primes, n):         
    if n >= 10000:
        return 0    
    if tested_items.has_key(n):        
        return tested_items[n]    
    tested_items[n] = sum(map(lambda x: x if n%x == 0 else 0, range(1,n/2+1)))        
    return tested_items[n]    

def sum_ammicable(primes, n):    
    dn = sum_proper_factors(primes, n)
    if tested_items.has_key(dn):        
        if tested_items[dn] == n and n != dn:
            print "found:", n
            return n
    else:
        db = sum_proper_factors(primes, dn)
        if db == n  and n != dn:
            print "found:", n
            return n
    return 0
    
def solve(target):    
    primes = myprimes.Primes()
    target_range = range(1,target)
    def check_am(n):
        return sum_ammicable(primes, n)
    print sum(map(check_am,target_range))    
    
print cProfile.run('solve(10000)')