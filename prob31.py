import math
import cProfile
      
def solve(target, vals):
    count = 0
    for val in vals:
        offset = 1
        if target%val == 0:
            count+= 1
        while target > val * offset:
            count += solve(target-val*offset, vals[vals.index(val)+1:])
            offset += 1    
    return count
    
print solve(200,[200,100,50,20,10,5,2,1])


#brute force, go!