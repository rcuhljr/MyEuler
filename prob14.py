import math
import cProfile
import array

#n = n/2 when even
#n = 3n+1 when odd

pairs = {1:1}

def compute(n):    
    try:
        temp = pairs[n]
    except:        
        pairs[n] = compute(nextItem(n))+1        
    return pairs[n]

def compute3(n):    
    if not pairs.has_key(n):        
        pairs[n] = compute3(nextItem(n))+1        
    return pairs[n]    
    
def nextItem(n):
    if n%2 == 0:
        return n/2
    return 3*n+1

def solve(target):
    traceTree = (compute3(i) for i in range(1,target))    
    print find_key(max(traceTree))

def find_key(val):
    for key in pairs.keys():
        if pairs[key] == val:
            return key
    
def solve2(target):
    pairs2[1] = 1
    traceTree = [compute2(i) for i in range(1,target)]        
    print traceTree.index(max(traceTree))

print cProfile.run('solve(1000000)')

#create a tuple of key, length, next value, shortcircuit as applicable.
#test with a straight one million array, see if it's faster, I think the slowdown will be in finding 
#if the item is in the hash already.
