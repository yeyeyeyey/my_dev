def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and li[j]>tmp:
            li[j+1] = li[j]
            j-=1
        li[j+1] = tmp
        print(li)
li = [234,1,43,6546,4645,2,235,543,62,5,34]

print(li)
insert_sort(li)