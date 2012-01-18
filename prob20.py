import math
import cProfile
   
def solve(n):    
    bignum = str(math.factorial(n))
    sum = 0
    for char in bignum:
        sum += int(char)
    print sum 
    
print cProfile.run('solve(100)')

#trying the naive solution