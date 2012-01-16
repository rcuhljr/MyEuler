import math
import cProfile
   
def solve(sum):
    c = sum - 3
    a, b = 1, 2
    
    while a**2+b**2 != c**2:               
        a += 1
        b -= 1
        if a >= b:            
            c -= 1
            b = sum-c-1
            a = 1
    print a*b*c

print cProfile.run('solve(1000)')

#initial thoughts. there is definitely an upper bound on c around .5 to .75 of the sum.
# the smallest c is .33c+1 332, 333, 334
