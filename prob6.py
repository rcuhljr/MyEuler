def sq(a):
    return a**2

def solve(x):
    values = range(1,x+1)
    print sum(values)**2-sum(map(sq,values))

solve(100)
#Hmmmm. 
#14 1^2+2^2+3^2
#36 (1+2+3)^2
#22