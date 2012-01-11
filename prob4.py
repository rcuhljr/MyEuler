import itertools
import cProfile
        
def solve(x):
    values = itertools.combinations(range(10**(x-1),10**x),2)
    maxpal = 0
    for n in values:
        value = n[0]*n[1]
        if value > maxpal and value == int(str(value)[::-1]):
            maxpal = value            
    print maxpal

print cProfile.run('solve(3)')

#made a mistake by not cutting out solutions of less then n digits as well as by making a poor assumption
#and not checking value>maxpal