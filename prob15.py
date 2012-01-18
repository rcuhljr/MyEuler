import math
import cProfile
   
def solve(side):    
    print math.factorial(side*2)/(math.factorial(side)**2)


print cProfile.run('solve(20)')

#I'm pretty sure there's a simple way to deal with this involving disco.

#2 rights
#2 downs

#so arrange four things which are in 2 identical groups is 4!/(2!*2!)

