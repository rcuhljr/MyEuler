import math
import cProfile
import itertools
      
def solve():
    solutions = {}
    terms = itertools.permutations("123456789")
    for n in terms:
        nstr = ''.join(n)
        for mindex in range(1,6):
            for eindex in range(mindex+1,9):
                mcand = nstr[0:mindex]
                mplier = nstr[mindex:eindex]
                prod = nstr[eindex:]                
                if int(mcand)*int(mplier) == int(prod):
                    solutions[int(prod)] = 0                
    print solutions
    print sum(map(lambda x: x, solutions.keys))
    
    
print solve()


#brute force, go!