import cProfile

class Lcm:
    def __init__(self, baseValue):
        self.base = baseValue    
        self.current = self.base
    def increment(self):
        self.current += self.base

def attach(x):
    return Lcm(x)
    
def clean(x):
    x = x[::-1]
    result = []
    for n in x:
        for existing in result:
            if existing%n == 0:
                break
        else:
            result.append(n)
    return result
    
def solve(x):
    customrange = clean(range(2,x+1))
    print customrange
    values = map(attach,customrange)    
    loop = True    
    while loop:    
        loop = False        
        minValue = values[0].current
        toIncrement = []
        for lcm in values:                            
            if minValue != lcm.current:
                loop = True
            if minValue > lcm.current:
                minValue = lcm.current
                toIncrement = []
            if minValue == lcm.current:
                toIncrement.append(lcm)
        if not loop:
            print minValue
        else:
            for lcm in toIncrement:
                lcm.increment()
    
        
def solve2(x):
    customrange = clean(range(2,x+1))
    print customrange
    print reduce(lcm, customrange)

def lcm(a, b):
    return a*b/gcd(a,b)

def gcd(a, b):
    #Thanks wiki!
    while b:
        a, b = b, a % b
    return a

print cProfile.run('solve2(20)')

#ignoring the optimization for now that I should increase all tied values, instead of just one.
#ignoring it no longer seemed feasible, saved about 50% runtime.
#solving 20 is slow... going to trim redundancies
#leaving old solution in place (took 500~ seconds to solve), but I'm going to switch to a gcd/lcm approach.
#oh lord that's depressing, .002 seconds.