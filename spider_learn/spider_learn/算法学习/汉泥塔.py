
def hanoi(n,a,b,c):
    s = 0
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s"%(a,c))
        hanoi(n-1,b,a,c)
        s+=1
hanoi(2,'A','B','C')
print(2**64)