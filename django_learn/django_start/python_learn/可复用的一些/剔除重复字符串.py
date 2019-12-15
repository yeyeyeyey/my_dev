a = ['a','a','dsd',4234,'sd','dsd']
b=[]
c=set(a)
for i in a:
    if i not in b:
        b.append(i)
print(b)
print(c)