
def factors(x):
"""returns a list of factors of x"""
    facs = {1,x}
    t = x-1
    r = 2
    while t >= r:
        if x % r == 0:
            facs.add(r)
            facs.add(int(x/r)) 
            t = int(x/r)  
        r += 1 
    facs.sort()
    return facs    
    
    
    