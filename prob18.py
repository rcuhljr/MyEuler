import math
import cProfile
   
def solve(file):
    grid = loadGrid(file)
    grid.reverse()
    previousRow = [0 for i in range(len(grid[0]))]
    for row in grid:
        width = len(row)
        newRow = []
        if width > 1:
            for n in range(width-1):                
                if(row[n]+previousRow[n] > row[n+1]+previousRow[n+1]):
                    newRow.append(row[n]+previousRow[n])
                else:
                    newRow.append(row[n+1]+previousRow[n+1])
            previousRow = newRow        
        else:            
            print row[0]+previousRow[0]
    

def loadGrid(file):
    result = []
    fin = open(file, 'rb')
    for line in fin:
        result.append(map(lambda x: int(x),line.rstrip().split(" ")))
    return result    

print cProfile.run('solve(\'prob18.txt\')')


#seems relatively straightforward if my solver is correct.