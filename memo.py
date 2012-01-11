import functools
def memo(func):
    cache = {}
    @functools.wraps(func)
    def wrap(*args):
        if args not in cache:
#            print "miss"
            cache[args] = func(*args)
#        else:
#            print "hit"
        return cache[args]
    return wrap
    
#Debugging to verify that caching was working