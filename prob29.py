import math
import cProfile
import itertools
      
def solve(min, max):    
    terms = (itertools.product(range(min,max+1),range(min,max+1)))
    def fun(a, b):        
        return a**b
    products = map(lambda x: fun(x[0],x[1]), terms)    
    products.sort()     
    previous = 0
    solution = {}
    for item in products:
        solution[item] = 0
        
    print len(solution)
        
    
    
print cProfile.run('solve(2,100)')

#brute force, go!