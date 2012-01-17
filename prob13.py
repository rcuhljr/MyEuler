import math
import cProfile
   
def solve(file):
    grid = loadGrid(file)         
    sum = 0;
    for x in grid:
        sum += x    
    print str(sum)[0:10]

def loadGrid(file):
    result = []
    fin = open(file, 'rb')
    for line in fin:
        result.append(int(line.rstrip()))
    return result    

print cProfile.run('solve(\'prob13.txt\')')


#lets see if pythons int can handle this.