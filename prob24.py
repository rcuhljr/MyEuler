import math
import cProfile
import itertools
   
def solve():    
    permutations = itertools.permutations("0123456789",10)    
    count = 1
    for char in permutations:
        if count == 1000000:
            print char
        count+=1
    
    
print cProfile.run('solve()')

#verifying hand solution.