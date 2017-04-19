def factors(x):
    if x == 1 : return [1]
    facs = [1,x]
    t = x-1
    r = 2
    while t > r:
        if x % r == 0:
            facs.append(r)
            if r != int(x/r) : facs.append(int(x/r)) 
            t = int(x/r)  
        r += 1 
    facs.sort()
    return facs   
    
    