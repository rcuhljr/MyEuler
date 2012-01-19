import cPickle as pickle
import math

class Primes:       

    def __init__(self):        
        try:
            self.primes = pickle.load( open( "primes.p", "rb"))                                
        except IOError:
            self.primes = [2, 3]
        try:
            self.divisors = pickle.load( open( "divisors.p", "rb"))                                
        except IOError:
            self.divisors = {1:[]}    
            
    def __del__(self):
        pickle.dump(self.primes, open("primes.p", "wb"))    
        pickle.dump(self.divisors, open("divisors.p", "wb"))
        
    #Return prime N. prime(1) = 2, prime(2) = 3...
    def prime(self, n):           
        if(len(self.primes) >= n):
            return self.primes[n-1]                        
        #find the value, we don't have it.    
        count = self.primes[len(self.primes)-1]
        while len(self.primes) < n:
            count += 2        
            self.pump_prime(count)            
        return self.primes[n-1]
        
    def pump_prime(self, x):
        cutoff = math.sqrt(x)
        for n in self.primes:
            if x%n == 0:
                return 
            elif n > cutoff:
                break
        self.primes.append(x)        
        
    def proper_divisors(self, number):
        if self.divisors.has_key(number):
            return self.divisors[number]
        def find_primes(n):
            result = [1]
            cutoff = n/2
            iter = 1
            val = 0
            while val < n:
                val = self.prime(iter)
                if n%val == 0:            
                    result.append(val)
                    n /= val
                iter += 1     
            return result
        divisors = find_primes(number)
        result = []
        for divisor in divisors:            
            if divisor == 1:
                result.append(1)
                continue                       
            mult = divisor*2
            if divisor != number:
                result.append(divisor)
            while number > mult:                
                if number%mult==0 and mult not in result:
                    result.append(mult)
                mult += divisor             
        result.sort()
        self.divisors[number] = result
        return result
        