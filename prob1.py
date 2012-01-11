result = 0
def f(x): 
    if x%3 == 0 or x%5 == 0:
        return x
    else:
        return 0
result = sum(map(f,range(1000)))
print result
#I've got a feeling that for awhile my code is just going 
#to be the ruby way in python until I get a better feel for the language.
#Time est 10-15 minutes of googling 'python map' 'python if'