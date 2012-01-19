import math
import cProfile
   
def solve(file):
    names = loadGrid(file)
    names.sort()
    def name_value(name, index):        
        return sum(map(lambda x: ord(x) - 64, name))*(index+1)
    
    print sum((name_value(name,index) for index,name in enumerate(names)))
    

def loadGrid(file):
    result = []
    fin = open(file, 'rb')
    for line in fin:
        result = line.rstrip().replace("\"","").split(",")
    return result    

print cProfile.run('solve(\'names.txt\')')


#seems relatively straightforward if my solver is correct.