e = 3
n = 0
for i in range(1,5):
    l = []   
    for j in range(1,i+1):
        n += 1
        l.append(str(n))
    print(" "*e," ".join(l),sep="")    
    e -= 1