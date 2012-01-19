import math
import cProfile
import itertools
   
def solve():    
    curr = 1
    prev = 1
    count = 2
    while len(str(curr)) < 1000:
        curr, prev, count = curr+prev, curr, count + 1
    print count
        
    
    
print cProfile.run('solve()')

#simple brute force?