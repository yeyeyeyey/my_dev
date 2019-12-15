li = [1,2,3,4,5,6,7,8,9,10,324,52,4,24,5241]
print(len(li))
# a = [i for i in li if i %2 !=0]
for i in li:
    if i%2 !=0:
        li.remove(i)
        print(li)
li.remove(10)
print(li)