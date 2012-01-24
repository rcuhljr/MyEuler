import math
import cProfile
      
def solve(pow):   
    def fun(n, power):        
        temp = sum(map(lambda x: int(x)**power, str(n)))        
        return temp
        
    nines = 9    
    while fun(nines, pow) > nines:
        nines = nines * 10 + 9
    results = []
    for n in range(2, nines):        
        if fun(n,pow) == n:
            results.append(n)
    print sum(results)
    
print cProfile.run('solve(5)')

#brute force, go!