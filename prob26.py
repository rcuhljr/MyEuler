import math
import cProfile
from decimal import *

def find_repeat(inFrac):
    frac = str(inFrac)[2::][:-1]    
    for i, n in enumerate(frac):            
        sol = repeats (n, frac[i::])
        if sol > 0:
            return sol
    return 0
        
def repeats(start, remainder):
    if len(remainder.replace(start, "")) == 0:
        return 1
    for gap in range(2,len(remainder)/2):        
        if start == remainder[gap]:            
            repeats = True
            for x in range(1, gap):
                if len(remainder)-1 < (gap+x):                    
                    break
                if remainder[x] != remainder[gap+x]:
                    repeats = False
                    break            
            if repeats:
                return gap
    return 0
def solve(target):    
    getcontext().prec = 2000
    one = Decimal(1)
    max = (1,0,0)
    for n in range(1, target):
        length = find_repeat(one/Decimal(n))
        if length > max[2]:
            max = (n, one/Decimal(n), length)
    print max[0], max[2], max[1]
        
    
    
#print cProfile.run('solve(10)')
solve(1000)

#simple brute force?
#really not happy with this solution, but meh.