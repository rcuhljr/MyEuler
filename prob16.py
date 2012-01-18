import math
import cProfile
   
def solve(number):    
    sum = 0
    for n in str(number):
        sum += int(n)
    print sum
    
print cProfile.run('solve(2**1000)')

#trying the naive solution