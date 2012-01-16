import cPickle as pickle
import math

class Primes:       

    def __init__(self):        
        try:
            self.primes = pickle.load( open( "primes.p", "rb"))                    
        except IOError:
            self.primes = [2, 3]
            
    def __del__(self):
        pickle.dump(self.primes, open("primes.p", "wb"))    
        
    #Return prime N. prime(1) = 2, prime(2) = 3...
    def prime(self, n):           
        if(len(self.primes) >= n):
            return self.primes[n-1]                        
        #find the value, we don't have it.    
        count = self.primes[len(self.primes)-1]
        while len(self.primes) < n:
            count += 2        
            self.pumpPrime(count)            
        return self.primes[n-1]
        
    def pumpPrime(self, x):
        cutoff = math.sqrt(x)
        for n in self.primes:
            if x%n == 0:
                return 
            elif n > cutoff:
                break
        self.primes.append(x)        