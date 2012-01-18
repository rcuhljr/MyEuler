import math
import cProfile

ones = {1:3, #one
        2:3, #two
        3:5, #three
        4:4, #four
        5:4, #five
        6:3, #six
        7:5, #seven
        8:5, #eight
        9:4  #nine
        }
teen = {0:3, #ten
        1:6, #eleven
        2:6, #twelve
        3:8, #thirteen
        4:8, #fourteen
        5:7, #fifteen
        6:7, #sixteen
        7:9, #seventeen
        8:8, #eighteen
        9:8  #nineteen
        }
tens = {
        2:6, #twenty
        3:6, #thirty
        4:5, #forty
        5:5, #fifty
        6:5, #sixty
        7:7, #seventy
        8:6, #eighty
        9:6  #ninety
        }
def count(n):    
    #print "counting:",n
    if n == 1000:
        return 11 #one thousand    
    sum = 0    
    if 99 < n:
        sum += ones[int(str(n)[0])] + 7 #hundred
        n = int(str(n)[1::])        
        if n > 0:
            sum += 3 #and
    if 19 < n < 100:
        sum += tens[int(str(n)[0])]
        n = int(str(n)[1::])
    if 9 < n < 20:
        sum += teen[int(str(n)[1])]
    if 0 < n < 10:
        sum += ones[n]
    #print sum
    return sum
        
        
def solve(number):    
    gen = (count(n) for n in range(1,number+1))
    print sum(gen)
    
print cProfile.run('solve(1000)')

#trying the naive solution