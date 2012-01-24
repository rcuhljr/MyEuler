import math
import cProfile
      
def solve(side):    
    max = side**2
    sum = 1
    current = 1
    step = 0
    offset = 0
    while current < max:
        if step == 0:
            offset += 2
        step += 1
        if step == 4:
            step = 0                        
        current += offset
        sum += current        
    print sum
        
    
    
print cProfile.run('solve(1001)')

#brute force, go!