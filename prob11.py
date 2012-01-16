import math
import cProfile
   
def solve(file):
    grid = loadGrid(file)     
    m, n = len(grid[0]), len(grid)
    maxval = 0
    for x in range(m):
        for y in range(n):
            maxval = max(maxval, checkNeighbors(x, y, grid))
    print maxval

def checkNeighbors(x, y, grid):
    xvals = [ 1, 1, 1, 0]    
    yvals = [-1, 0, 1, 1]
    m, n = len(grid[0]), len(grid)    
    def checkdir(xstep, ystep):
        if(xstep > 0 and x+3 >= m):
            return 0
        if(ystep > 0 and y+3 >= n):
            return 0
        if(ystep < 0 and y-3 < 0):
            return 0        
        return reduce(lambda a, b: a*b,[int(grid[y+ystep*b][x+xstep*a]) for (a,b) in zip(range(4),range(4))])
    return max(map(checkdir, xvals, yvals))
    
def loadGrid(file):
    result = []
    fin = open(file, 'rb')
    for line in fin:
        result.append(line.rstrip().split(' '))
    return result    

print cProfile.run('solve(\'prob11.txt\')')

#initial thoughts, move through the grid right to left, top to bottom, checking 4 down, 4 right, and 8 diagonal (up and down right) as grid bounds permit
#this will hit all the possible combinations without any duplication I believe.
# 0 = grid space X = check, T = current square.
#   OOOOOOOXO
#   OOOOOOXOO
#   OOOOOXOOO
#   OOOOTXXXO
#   OOOOXXOOO
#   OOOOXOXOO
#   OOOOXOOXO



